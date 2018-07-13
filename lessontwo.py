import random
import os
from pandas import DataFrame,read_csv
import pandas as pd
import matplotlib.pyplot as plt
#create data

names=['Bob','Jessica','Mary','John','Mel']

random.seed(500)
random_names =[random.choice(names)for i in range(1000)]
#print(random_names[:10])
births =[random.randint(1,100)for i in range(100)]
#print(births[:10])
#merge the two lists
babydataset=list(zip(random_names,births))
# create a dataframe
df= pd.DataFrame(data=babydataset,columns=["Names","Births"])
#print(df[:15])
#to export df to csv file
df.to_csv('births1881.csv',index=False,header=False)
#pull/get the csv file
Location= r'/home/ema564/PycharmProjects/first/births1881.csv'
getd=pd.read_csv(Location,names=['Names','Births'])
print(getd.tail())
#delete the txt file ,now dat we are using
os.remove(Location)
print(getd['Names'].describe())
#groupby names
grouped =getd.groupby('Names')
print(grouped.sum())
#sort births
sorted=getd.sort_values(['Births'],ascending='False')
print(sorted.head(2))


sorted.head().plot()

plt.show()
