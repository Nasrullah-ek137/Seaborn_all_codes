'''Box plot '''

import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset('tips')
#print(data)

sns.boxplot(x='day',y='total_bill',order=['Fri','Sat','Thur','Sun'],showmeans=True,data=data)

plt.show()