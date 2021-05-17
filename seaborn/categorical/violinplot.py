import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset('penguins')

sns.catplot(data=penguins, x="species", y="bill_length_mm", kind="violin")

sns.catplot(data=penguins, x="species", y="bill_length_mm", kind="violin", hue="sex")

sns.catplot(data=penguins, x="species", y="bill_length_mm", kind="violin", hue="sex", split=True)

plt.show()