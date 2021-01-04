import pandas as pd

#读取数据
df=pd.read_excel(r'C:\Users\nyy\Desktop\数据.xlsx',index_col='Idxtrd01')

#计算收益率
result=df['Idxtrd05'].pct_change(periods=1,axis=0)


print(result)
