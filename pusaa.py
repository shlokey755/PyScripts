import matplotlib.pyplot as plt
x = [1,2,5,6,8]
y1 = [2,4,6,8,10]
y2 = [1,2,3,4,5]
y3 = [3,6,9,12,15]
y4 = [y1,y2,y3]
plt.plot(x,y1,label = 'Normal')
plt.plot(x,y2,label = 'Slow')
plt.plot(x,y3,label = 'Fast')
plt.legend()
plt.show()
