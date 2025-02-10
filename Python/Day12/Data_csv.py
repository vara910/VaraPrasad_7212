import pandas as pd
df=pd.read_csv('customer.csv')
print(df)
print(df[['First Name','Email']])       #filtering a separate column
grp=df.groupby('Country').count()
print(grp)
df2=pd.read_csv('customer.csv')
jssso=df2.to_json('customer_updated.json',index=False)
print(jssso)