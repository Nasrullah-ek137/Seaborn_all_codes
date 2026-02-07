'''Bar plot using seaborn'''

import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset('penguins').head(300)
#print(data)

sns.barplot(x='island',y='bill_length_mm',data=data,hue='sex',order=['Dream','Torgersen','Biscoe'],hue_order=['Female','Male'])
plt.title('This is bar plot')
plt.show()