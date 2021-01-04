import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdate

#读取文件
df=pd.read_excel(r'C:\Users\nyy\Desktop\数据.xlsx')
df.index=pd.to_datetime(df['Idxtrd01'],format='%Y-%m')

# 字体嵌入
mpl.rcParams['font.family']='Kaiti'

#绘制图形
df['Idxtrd03'].plot(label='最高价')
df['Idxtrd04'].plot(label='最低价')

#x轴处理，显示每一个月份
plt.gca().xaxis.set_major_locator(mdate.MonthLocator(interval=1))

#设置标题，轴标签
plt.title('制沪深300指数2019年的最高价和最低价曲线',fontsize=18)
plt.xlabel('时间/月')
plt.ylabel('价值/元')

#显示图例和图
plt.legend()
plt.show()
