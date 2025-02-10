import pandas as pd
# remove.os()
data={
    
    'state':['bihar','himachal','tamilnadu','kerala','odisha','westbengal'],
    'year':[2021,2022,2045,2023,2025,2027],
    'sales':[20000,21000,23443,32534,23523,86345],
    'profit':[3002,2345,4556,4345,5675,3452],
    'Region':['North','North','South','South','east','east']
}
df=pd.DataFrame(data)
df.set_index(['Region'],inplace=True)
# print(df.loc[('South'),'sales'])
# print(df)
df_sales=pd.DataFrame({'state':['kerala','odisha','westbengal'],
                       'sales':[32534,23523,86345]})
df_profits=pd.DataFrame({'state':['kerala','odisha','westbengal'],
                         'profit':[4345,5675,3452]})
df_merged=pd.merge(df_sales,df_profits,on='state',how='right')
print(df_merged)