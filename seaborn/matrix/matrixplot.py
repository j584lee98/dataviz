import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

flights = sns.load_dataset('flights')

pivot_flights = pd.pivot_table(data=flights, values='passengers', index='month', columns='year')

sns.heatmap(data=pivot_flights)

plt.show()

sns.heatmap(data=pivot_flights, annot=True, fmt="d")

plt.show()

sns.heatmap(data=pivot_flights, cmap="coolwarm")

plt.show()

sns.heatmap(data=pivot_flights, cmap="Greys")

plt.show()