import matplotlib.pyplot as plt
import numpy as np
xvals = np.arange(-2,1,0.01)
newyvals = 1 - 0.5 * xvals**2
plt.plot(xvals,newyvals,'b--')
plt.title('Example plots')
plt.xlabel('Input')
plt.ylabel('Function values')
plt.show()
