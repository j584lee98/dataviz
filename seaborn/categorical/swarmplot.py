import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset('penguins')

sns.catplot(data=penguins, x="species", y="bill_length_mm", kind="swarm")

sns.catplot(data=penguins, x="species", y="bill_length_mm", kind="swarm", hue="sex")

sns.catplot(data=penguins, x="species", y="bill_length_mm", kind="swarm", hue="sex", split=True)

plt.show()