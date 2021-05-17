import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x_arr = np.arange(0,11)
y_arr = x_arr**2

figure = plt.figure()

axes1 = figure.add_axes([0.1,0.1,0.8,0.8])
axes2 = figure.add_axes([0.2,0.5,0.3,0.3])

axes1.plot(x_arr, y_arr, 'r--')
axes1.set_xlabel('X')
axes1.set_ylabel('Y')
axes1.set_title('x^2')

axes2.plot(y_arr, x_arr, 'b--')
axes2.set_xlabel('X')
axes2.set_ylabel('Y')
axes2.set_title('sqrt(x)')

plt.show()