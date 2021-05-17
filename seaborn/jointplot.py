import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

sns.jointplot(data=tips, x='total_bill', y='tip') # default scatter

plt.show()

sns.jointplot(data=tips, x='total_bill', y='tip', kind='reg')

plt.show()

sns.jointplot(data=tips, x='total_bill', y='tip', kind='resid')

plt.show()

sns.jointplot(data=tips, x='total_bill', y='tip', kind='hex')

plt.show()

sns.jointplot(data=tips, x='total_bill', y='tip', hue='sex')

plt.show()

sns.jointplot(data=tips, x='total_bill', y='tip', hue='sex', kind='hist')

plt.show()

sns.jointplot(data=tips, x='total_bill', y='tip', hue='sex', kind='kde')

plt.show()