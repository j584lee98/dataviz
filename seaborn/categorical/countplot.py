import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset('penguins')

sns.catplot(data=penguins, x="species", kind="count")

sns.catplot(data=penguins, x="species", kind="count", hue="sex")

plt.show()