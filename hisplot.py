'''Histogram plot using seborn'''

import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset('penguins').head(250)
#print(data)

sns.displot(data['body_mass_g'],bins=[2500,3000,3500,4000,4500,5000,5500,6000,6500],color='m',kde=True,label='Histogram-bar')
plt.title('This is histogram-Plot')
plt.xlabel('Prices')
plt.ylabel('No.of People')
plt.legend()
plt.show()
