'''Strip Plot'''
import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset('tips')
#print(data)

sns.stripplot(x='day',y='total_bill',hue='sex',jitter=10,data=data)
plt.show()