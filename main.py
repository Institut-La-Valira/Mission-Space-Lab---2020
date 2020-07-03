# 2020 Astro Pi Mission Space Lab
# Institut La Valira - La Seu d'Urgell - Catalunya - Spain
# Code: lavalira
# Calculation of magnetic field, orientation, acceleration, rotation and latitude and longitude of the ISS
# Created by: Ruben Jimenez, Laia Sala, Isabel Canut, Aina Izquierdo, Pau Calvet and Markus Urban 

# Import the libraries
import csv
from datetime import datetime
import os
import time
from time import sleep
from ephem import readtle, degree



# Establish connection with the SenseHat sensors
sense = SenseHat()

# Definitons for the display 
sense.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (155,155,155)
nothing = (0,0,0)
pink = (255,105, 180)

def M1():
    R = green
    W = yellow
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    W, W, O, O, O, O, R, R,
    W, W, W, O, O, R, R, R, 
    W, W, W, B, B, R, R, R,
    W, W, O, B, B, O, R, R,
    W, W, O, O, O, O, R, R,
    W, W, O, O, O, O, R, R,
    W, W, O, O, O, O, R, R,
    ]
    return logo

def M2():
    W = green
    R = red
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    W, W, O, O, O, O, R, R,
    W, W, W, O, O, R, R, R, 
    W, W, W, W, R, R, R, R,
    W, W, O, W, R, O, R, R,
    W, W, O, O, O, O, R, R,
    W, W, O, O, O, O, R, R,
    W, W, O, O, O, O, R, R,
    ]
    return logo
def M3():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    W, W, O, O, O, O, W, W,
    W, W, W, O, O, W, W, W, 
    W, W, W, W, W, W, W, W,
    W, W, O, W, W, O, W, W,
    W, W, O, O, O, O, W, W,
    W, W, O, O, O, O, W, W,
    W, W, O, O, O, O, W, W,
    ]
    return logo

def M4():
    W = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    W, W, O, O, O, O, W, W,
    W, W, W, O, O, W, W, W, 
    W, W, W, W, W, W, W, W,
    W, W, O, W, W, O, W, W,
    W, W, O, O, O, O, W, W,
    W, W, O, O, O, O, W, W,
    W, W, O, O, O, O, W, W,
    ]
    return logo

def M5():
    W = pink
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    W, W, O, O, O, O, W, W,
    W, W, W, O, O, W, W, W, 
    W, W, W, W, W, W, W, W,
    W, W, O, W, W, O, W, W,
    W, W, O, O, O, O, W, W,
    W, W, O, O, O, O, W, W,
    W, W, O, O, O, O, W, W,
    ]
    return logo

images = [M1,M2,M3,M4,M5]
count = 0

# Display definition end here


# Get the start time of the mission
start_time = time.time()

# Define the period of the mission (in seconds)
period_of_time = 10680




# Latest ISS orbital elements (14/02/2020)
name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   20045.18587073  .00000950  00000-0  25302-4 0  9990"
line2 = "2 25544  51.6443 242.0161 0004885 264.6060 207.3845 15.49165514212791"


iss = readtle(name, line1, line2)


# Measurements will be saved in the current working directory into a file named data01.csv
dir_path = os.path.dirname(os.path.realpath(__file__))

data_file = dir_path + '/data01.csv'


# We write the heading of the data file
with open(data_file, 'w') as f:
    writer = csv.writer(f)
    header = ("Date/time", "X", "Y" , "Z" , "PITCH", "ROLL", "YAW", "ACC_X", "ACC_Y", "ACC_Z","GYRO_X","GYRO_Y","GYRO_Z","LAT","LONG")
    writer.writerow(header)
    i=0
    
# Beginning of the data register iteration 
while time.time() < start_time + period_of_time:

# We get the magnetic field data    
    magnetic = sense.get_compass_raw()
   
    x = magnetic['x']
    y = magnetic['y']
    z = magnetic['z']


    # 4 decimal round    
    x=round(x, 4)
    y=round(y, 4)
    z=round(z, 4)
    
    # We get the orientation in degrees
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
    
    # 6 decimal round
    pitch=round(pitch, 6)
    roll=round(roll, 6)
    yaw=round(yaw, 6)
    
    # We get acceleration in Gs
    acceleration = sense.get_accelerometer_raw()
    xa = acceleration['x']
    ya = acceleration['y']
    za = acceleration['z']
    
    # 6 decimal round
    xa=round(xa, 6)
    ya=round(ya, 6)
    za=round(za, 6)

    # We get the rotational intensity of the axis in radians per second
    gyro = sense.get_gyroscope_raw()
    xgyro = gyro["x"]
    ygyro = gyro["y"]
    zgyro = gyro["z"]
    
    # 6 decimal round
    xgyro=round(xgyro, 6)
    ygyro=round(ygyro, 6)
    zgyro=round(zgyro, 6)    

    # From the current moment, this function computes the ISS latitude and longitude
    iss.compute()
    
    # Converts the data to degrees
    isslat = iss.sublat/degree
    isslong = iss.sublong/degree
    
    # 4 decimal round
    isslat=round(isslat,4)
    isslong=round(isslong,4)
    
    
    # Creates the row that will be written in the data file with all the measurements
    row = (datetime.now(), x, y, z,pitch,roll,yaw,xa,ya,za,xgyro,ygyro,zgyro,isslat,isslong)
    
    # We open the data file and write the row in it with csv format
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)
        
    # Display the data into shell while we are testing the program (do not use it in real execution)    
    #print("x={0}, y={1}, z={2}, pitch={3}, roll={4}, yaw={5}, acc_x={6}, acc_y={7}, acc_z={8} , gyro_x={9} , gyro_y={10} , gyro_z={11} , latitud={12} , longitud={13}".format(x, y, z, pitch, roll, yaw, xa, ya, za, xgyro, ygyro, zgyro, iss.sublat / degree, iss.sublong / degree))
    
    # i and j are variables that control the display frequency
    i+=1

    # For every 50 cycles it displays "M" (from Magnetic Field) in different colors on the screen
    j=i%50
    

    if j<1:
        sense.set_pixels(images[count % len(images)]())
        
        count += 1

# When 3 hours have passed, the program closes itself
sense.show_message("bye bye, by La Valira")
exit()
