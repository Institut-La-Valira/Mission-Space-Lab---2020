import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random
import xlrd

print('     Inicialitzant el programa')

loc = (r"C:\Users\murba\Documents\INSTITUT\Matemàtiques\ASTRO_PI_PROJECT\python\tests\MATPLOTLIB\nostre.xlsx") 


wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)

print('     A punt de començar')

# A contrinuació farem algunes llistes per fer la llegenda

classes = ['From 0 to 9','From 10 to 19','From 20 to 29', 'From 30 to 39', 'From 40 to 49', 'Bigger as 50']
class_colours = ['#02ABDE','#67B1C7','#B3E1EF', '#EFB3B3', '#F56D6D', '#FF0000']
recs = []

  
# Ara sabrem el número total de files de l'excel

files = sheet.nrows

test = 500 # VARIABLE DE PROVA

vegada = 0
save = 0
cada200 = 0


for i in range(files):

    if vegada == 120:
        

        x = sheet.cell_value(i, 14)
        y = sheet.cell_value(i, 13)
        m = sheet.cell_value(i, 15)

        vegada = 0

       
        
        print(i)


        if m < 10:
            
            plt.scatter(x, y , c = '#02ABDE', s = 10)
            
            
        elif m < 20:

            plt.scatter(x, y , c = '#67B1C7', s = 10, label="b")

        elif m < 30:

            plt.scatter(x, y , c = '#B3E1EF', s = 10, label="m")

        elif m < 40:

            plt.scatter(x, y , c = '#EFB3B3', s = 10, label="a")
            
        elif m < 50:

            plt.scatter(x, y , c = '#F56D6D', s = 10, label="ma")

        elif m >= 50:

            plt.scatter(x, y , c = '#FF0000', s = 10, label="mma")
            
        
        

    else:

        vegada = vegada + 1

for i in range(0,len(class_colours)):
    recs.append(mpatches.Rectangle((0,0),1,1,fc=class_colours[i]))
plt.legend(recs,classes,loc=4)

plt.title("Figure 1: Magnetic field based on LAT and LONG")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.text(106, 22, "Start")
plt.text(32, 7, "End")

print('     Ja hem acabat. Disfruta del resultat!')
plt.show()

