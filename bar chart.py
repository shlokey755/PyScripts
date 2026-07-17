import matplotlib.pyplot as plt
plt.subplot(3,1,1)
plt.bar([2,3,8],[1,5,6])
plt.xticks([2,3,8])
plt.yticks([1,5,6])

plt.subplots_adjust(hspace = 0.8, wspace = 0.8)

plt.subplot(3,1,2)
plt.plot([2,3,8],[1,5,6])
plt.xticks([2,3,8])
plt.yticks([1,5,6])

plt.show()
