import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset('penguins')

sns.stripplot(data=penguins, x="species", y="bill_length_mm")

plt.show()