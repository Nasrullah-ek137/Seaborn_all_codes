import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Creating basic HeatMap
'''
arr=np.linspace(1,20,9).reshape(3,3)
#print(arr)
sns.heatmap(arr)
plt.show()

'''
# Advance HeatMap
data=sns.load_dataset('anagrams')
#print(data)

delete=data.drop(columns='attnr',axis=1).head(5)
#print(delete)


arr=np.array([['a1','a2','a3','a4'],['b1','b2','b3','b4'],['c1','c2','c3','c4'],['d1','d2','d3','d4'],
              ['e1','e2','e3','e4']])


items={'fontsize':10,'color':'r'}

sns.heatmap(delete,vmin=0,vmax=11,cmap='Accent',annot=arr,fmt='s',annot_kws=items,linewidths=5,linecolor='black',cbar=False
            ,xticklabels=False,yticklabels=False)
plt.title('This is HeatMap')
plt.show()