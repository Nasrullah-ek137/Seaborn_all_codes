'''Linear Plot using SeaBorn'''

'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var1=[1,2,3,4,5,6,7]
var2=[3,2,4,6,5,7,1]

df=pd.DataFrame({'var1':var1,'var2':var2})

sns.lineplot(x='var1 ',y='var2',color='y',marker='o',data=df)
plt.show()
'''

'''
import matplotlib.pyplot as plt
import seaborn as sns

var1=[1,2,3,4,5,6,7]
var2=[4,3,5,7,6,2,1]

sns.lineplot(x=var1,y=var2)
plt.show()'''



# Then go to ggogle and search 'Seaborn datasets' and down scroll see github 'data repository for seaborn eg' then click 
# and see various large datasets are here you can use.
# i am using one penguins.csv then i am load this data
# you don't need to download dataset you simple load dataset file data=sns.load_dataset('penguins')

'''
import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset('penguins')
sns.lineplot(x='bill_length_mm',y='bill_depth_mm',data=data)

plt.grid()
plt.show()'''

# Lineplot method
import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset('penguins').head(100)
#print(data)

sns.lineplot(x='bill_length_mm',y='bill_depth_mm',data=data,hue='sex',style='sex',palette='Accent')
plt.title('This is Line-Plot')
plt.grid()
plt.show()






# optional 
'''
import matplotlib.pyplot as plt
import pandas as pd

read=pd.read_csv('taxis.csv').head(50)
#print(read)

plt.plot(read['passengers'],read['fare'])
plt.show()'''