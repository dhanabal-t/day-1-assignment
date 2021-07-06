import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,10)
y=3*x+10
plt.plot(x,y,'ro--')
plt.xlabel('x-axis',color='blue')
plt.ylabel('y-axis',color='blue')
plt.title('2d-Diagram',color='blue')
