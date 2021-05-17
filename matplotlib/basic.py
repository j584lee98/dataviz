import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x_arr = np.arange(0,11)
y_arr = x_arr**2

figure = plt.figure()

axes = figure.add_axes([0.1,0.1,0.8,0.8])

axes.plot(x_arr, y_arr, 'r--')
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')

plt.show()