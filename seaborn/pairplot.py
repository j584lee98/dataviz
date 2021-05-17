import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

sns.pairplot(data=tips)

plt.show()

sns.pairplot(data=tips, hue="sex")

plt.show()