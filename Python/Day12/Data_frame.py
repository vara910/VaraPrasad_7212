import pandas as pd
data={
    'Name':['vara','vaish','vamshi','anurag','raju'],
    'Age':[21,22,23,24,26],
    'City':['newyork','Medchal','hyderabad','ghanpur','toopran']
}
df=pd.DataFrame(data)
print(df)
df.head()