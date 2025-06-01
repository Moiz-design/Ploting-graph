import numpy as np
import matplotlib.pylab as plt
x=np.random.rand(1,10)
y=np.linspace(1,10,10)
print(len(x),len(y))
col = ['r', 'm', 'y', 'b', 'g', 'k', 'c', 'pink', 'khaki', 'lime']
s=np.arange(1,100,10)
ax=plt.scatter(x,y,color=col,sizes=s)
plt.show()