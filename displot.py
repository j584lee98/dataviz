import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

sns.displot(tips['tip'])

plt.show()