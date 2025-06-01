import matplotlib.pyplot as plt
import numpy as np

x = [49 ,33, 26, 80, 10]
print(x)
y=['United States','Great Britan','Russia',' China','Germany',]
plt.clf()
ex=[0.0,0.0,0.0,0.01,0.0]
plt.subplots_adjust(top=0.9,right=1)
plt.pie(x,labels=y ,explode=ex , startangle=90,autopct='%1.1f%%',counterclock=False,center=(0.5, 0.6),)
plt.legend(fontsize=12,loc = 'center left', bbox_to_anchor=(-0.45, 0.6))

plt.title("Gold Medals of five most succesful company ",fontname= 'DejaVu Sans')

plt.show()
