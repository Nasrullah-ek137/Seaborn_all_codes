'''Pair Plot '''
import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset('tips')

sns.pairplot(data,hue='sex',markers=['*','o'],hue_order=['Female','Male']) # vars=['tip','total_bill','size']

plt.show()