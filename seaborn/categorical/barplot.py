import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset('penguins')

sns.catplot(data=penguins, x="species", y="body_mass_g", kind="bar")

sns.catplot(data=penguins, x="species", y="body_mass_g", kind="bar", hue="sex")

plt.show()