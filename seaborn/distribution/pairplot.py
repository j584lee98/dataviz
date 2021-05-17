import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

sns.pairplot(data=tips)

sns.pairplot(data=tips, hue="sex") # pairplot + hue

plt.show()