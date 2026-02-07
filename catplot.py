'''cat plot'''

import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset('tips')
#print(data)

sns.catplot(x='size',y='tip',hue='sex',kind='strip',data=data)

plt.show()