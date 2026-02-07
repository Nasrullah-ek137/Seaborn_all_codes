'''Viplinplot'''
import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset('tips')
#print(data)

sns.violinplot(x='day',y='total_bill',hue='sex',split=True,data=data)
plt.title('Violin Plot')
plt.show()