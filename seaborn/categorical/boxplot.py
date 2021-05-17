import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset('penguins')

sns.catplot(data=penguins, x="species", y="bill_length_mm", kind="box")

sns.catplot(data=penguins, x="species", y="bill_length_mm", kind="box", hue="sex")

plt.show()