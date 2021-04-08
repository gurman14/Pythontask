import pandas as pd

df=pd.read_excel("employee__1_.xls")  #Give the absolute local path to your file name

df['Date of Birth'] = pd.to_datetime(df['Date of Birth'])
df['Date of Joining'] = pd.to_datetime(df['Date of Joining'])

x=df.groupby('Quarter of Joining').apply(pd.DataFrame.sort_values, 'Date of Birth')

dict1={}
for i in range(0,len(x)):
    if x["Quarter of Joining"][i] in dict1.keys():
        dict1[x["Quarter of Joining"][i]].append(x["First Name"][i])
    else:
        dict1[x["Quarter of Joining"][i]]=[x["First Name"][i]]

print(dict1)







