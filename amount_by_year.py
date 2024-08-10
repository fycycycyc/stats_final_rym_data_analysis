import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator  # 确保正确导入 MaxNLocator

# 加载数据
data_90s = pd.read_csv('top100_90s_ja.csv')
data_00s = pd.read_csv('top100_00s_ja.csv')
data_10s = pd.read_csv('top100_10s_ja.csv')

# 合并数据
combined_data = pd.concat([data_90s, data_00s, data_10s])

# 按年份计算专辑数量
albums_per_year = combined_data['Release Year'].value_counts().sort_index()

# 绘制柱状图
plt.figure(figsize=(14, 7))
plt.bar(albums_per_year.index, albums_per_year.values, color='#05b387')
plt.xlabel('Year',fontsize=14)
plt.ylabel('Number of Albums',fontsize=14)
plt.title('Number of Albums Selected in the Top 100 for the 90s, 00s, and 10s',fontsize=16)
plt.xticks(albums_per_year.index,rotation=45)  # Rotate the x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

ax = plt.gca()  # 获取当前的坐标轴
ax.yaxis.set_major_locator(MaxNLocator(integer=True))  # 设置 y 轴主刻度为整数

#plt.tight_layout()  # 优化布局
plt.savefig('album_amount_by_year_japan.png', dpi=600)  # 保存为高分辨率
plt.show()
