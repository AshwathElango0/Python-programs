from matplotlib import pyplot as plt          #importing necessary modules
from random import choice
from math import sqrt
x_num_lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_num_lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x_dataset=[]                                   #generating datasets
y_dataset=[]
for i in range(10):
    x_choice=choice(x_num_lst)
    x_dataset.append(x_choice)
    x_num_lst.remove(x_choice)
    
for i in range(10):
    y_choice=choice(y_num_lst)
    y_dataset.append(y_choice)
    y_num_lst.remove(y_choice)
    
plt.plot(x_dataset[0:6], y_dataset[0:6], 'ro')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x_dataset[6::], y_dataset[6::], 'bo')


x_c=float(input("Enter x_c : "))          #point you wish to identify
y_c=float(input("Enter y_c : "))
coords=[]                                  #starting distance and color identification
for i in range(10):
    coords.append([x_dataset[i], y_dataset[i]])
red=0  
dists=[]
cc=coords[0]
for i in coords:
    x=(i[0]-x_c)**2
    y=(i[1]-y_c)**2
    dist=sqrt(x+y)
    dists.append(dist)
    if dist==min(dists):
        cc=i
        if i in coords[0:6]:
            red=1
        else:
            red=0
color=''            
if red==0:
    color='blue'
else:
    color='red'
    
        
print(f"Closest point on the graph is {cc}")          #output
print(f"Closest point on the graph is {color}")
if color=='blue':
    plt.plot(x_c, y_c, 'bo')
    plt.show()
else:
    plt.plot(x_c, y_c, 'ro')
    plt.show()
