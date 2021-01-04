import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


#读取数据
df=pd.read_excel(r'C:\Users\nyy\Desktop\数据.xlsx')
df.index=pd.to_datetime(df['Idxtrd01'],format='%Y-%m')

#字体嵌入
mpl.rcParams['font.family']='Kaiti'
df['Idxtrd03'].plot(label="最高价",color='red',linestyle='-')
df['Idxtrd04'].plot(label='最低价',color='blue',linestyle=':')

#月份精确处理
ax=plt.gca()
ax.xaxis.set_major_locator(mpl.dates.MonthLocator(interval=1))

#设置标题，轴标签
plt.title('2019年的最高价和最低价曲线',fontsize=20)
plt.xlabel('月份')
plt.ylabel('价格')

plt.legend()
plt.show()