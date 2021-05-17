import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x_arr = np.arange(0,11)
y_arr = x_arr**2

num_rows = 3
num_cols = 3

figure, axes = plt.subplots(num_rows, num_cols)

for i in range(num_rows):
  for j in range(num_cols):
    style = ''
    if j == 0:
      style = 'r-'
    elif j == 1:
      style = 'b--'
    else:
      style = 'gx-'
    
    axes[i, j].plot(x_arr, x_arr**(i+1), style)
    axes[i, j].set_xlabel('X')
    axes[i, j].set_ylabel(f'X^{i+1}')
    axes[i, j].set_title('Title')

plt.tight_layout()
plt.show()