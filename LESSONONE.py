from pandas import DataFrame,read_csv
import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib

#system and python packages versions being used
print('python version '+ sys.version)
print('pandas version '+ pd.__version__)
print('matplotlib version '+ matplotlib.__version__)

#creatind our own data set
names =['Bob','Jessica','Mary','john','Mel']
births = [968, 155,77,578, 973]
babydataset =list(zip(names,births))

#convert the data set created to a dataframe then to csv file
df= pd.DataFrame(data=babydataset,index=['a','b','c','d','e'],columns=['Names','Births'])
print(df.loc['a'])

df.to_csv('Births1880.csv',index=False,header=False)
#to get the data/ pull the csv file using "read_csv" function
Location = r'/home/ema564/PycharmProjects/first/Births1880.csv'
getd=pd.read_csv(Location,names=['Names','Births'])
print((getd))

#prepare data
getd.Names.dtypes
getd.dtypes
#analyze data 'find the most popular_name

sorted = getd.sort_values(['Births'],ascending=False)
(sorted.head(2))

#present data

#create graph
print(getd['Births'].plot())
#get maxvalue
MaxValue = getd['Births'].max()
#getthe name of the maxvalue
MaxName =getd['Names'][getd['Births'] == getd['Births'].max()]
#converting int to string
Text = str(MaxValue) + " - " + MaxName

#add text to graph
plt.annotate(Text,xy=(1,MaxValue),xytext=(8,0),xycoords=('axes fraction','data'),textcoords='offset points')

#print('the most popular name ')
getd[getd['Births']== getd['Births'].max()]
#plt.show()
