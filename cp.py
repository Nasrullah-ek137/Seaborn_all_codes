'''CountPlot using SeaBorn'''
import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset('tips')

sns.countplot(x='sex',hue='smoker',color='g',data=data)
plt.title('This is CountPlot')
plt.show()