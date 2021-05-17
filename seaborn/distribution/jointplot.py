import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

sns.jointplot(data=tips, x='total_bill', y='tip') # default scatter

sns.jointplot(data=tips, x='total_bill', y='tip', kind='reg')

sns.jointplot(data=tips, x='total_bill', y='tip', kind='resid')

sns.jointplot(data=tips, x='total_bill', y='tip', kind='hex')

sns.jointplot(data=tips, x='total_bill', y='tip', hue='sex')

sns.jointplot(data=tips, x='total_bill', y='tip', hue='sex', kind='hist')

sns.jointplot(data=tips, x='total_bill', y='tip', hue='sex', kind='kde')

plt.show()