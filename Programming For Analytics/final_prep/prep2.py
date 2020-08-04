import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
iris.head()

# barplot
iris.species.value_counts().plot(kind='bar')
# histogram
iris.petal_width.hist(bins=8)

# annotated plot
a = iris.petal_width.hist(bins=7, \
                        color='peru',
                        grid=False,
                        xlabelsize=12,
                        ylabelsize=12)

plt.xlabel('Petal Width', fontsize=15)
plt.xlim([0,3])
plt.ylabel('Frequency', fontsize=15)
plt.ylim([0,50])
plt.show()

a = a.get_figure()
a.savefig('barplot1.png', dpi=300)

# Sebastián Pastor Ferrari - 2019 ©
