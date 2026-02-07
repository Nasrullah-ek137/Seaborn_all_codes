'''Scatter plot using seaborn'''

import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset('penguins')
#print(data)

sns.scatterplot(x='bill_length_mm',y='bill_depth_mm',data=data,hue='sex',style='sex',sizes=(50,40),markers={'Male':'*','Female':'o'})

plt.title('This is scatter plot')
plt.grid()
plt.show()
