import pandas as pd
import matplotlib.pyplot as plt
import  matplotlib

#读取数据
df=pd.read_excel(r'C:\Users\nyy\Desktop\数据.xlsx')
df.index=pd.to_datetime(df['Idxtrd01'],format='%Y-%m')

#中文字体
plt.rcParams['font.sans-serif']=['Microsoft YaHei']

#计算收益率
df['Idxtrd05'].pct_change(periods=1,axis=0).plot(color='red',linestyle=':')

#月份精确处理
ax=plt.gca()
ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=1))

#适当的标题
plt.title('收益率曲线图',fontsize=20)
plt.xlabel('月份')
plt.ylabel('收益率')

plt.show()