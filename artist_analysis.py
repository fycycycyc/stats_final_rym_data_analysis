import pandas as pd
import matplotlib.pyplot as plt

# 确保导入了适合显示日语字符的字体
plt.rcParams['font.family'] = 'Microsoft YaHei'  # 设置为微软雅黑

# 加载数据
data_90s = pd.read_csv('top100_90s_ja.csv')
data_00s = pd.read_csv('top100_00s_ja.csv')
data_10s = pd.read_csv('top100_10s_ja.csv')

# 统计每个年代中入榜次数最多的艺术家
top_artists_90s = data_90s['Artist Name'].value_counts().head(5)
top_artists_00s = data_00s['Artist Name'].value_counts().head(5)
top_artists_10s = data_10s['Artist Name'].value_counts().head(5)

# 合并所有时间段的数据
combined_data = pd.concat([data_90s, data_00s, data_10s])
top_artists_all_time = combined_data['Artist Name'].value_counts().head(5)

# 可视化
fig, axs = plt.subplots(2, 2, figsize=(18, 12))  # 2x2排列

# 90年代
axs[0, 0].barh(top_artists_90s.index, top_artists_90s.values, color='skyblue')
axs[0, 0].set_title('Top 5 Artists in the 90s', fontsize=14)
axs[0, 0].invert_yaxis()

# 00年代
axs[0, 1].barh(top_artists_00s.index, top_artists_00s.values, color='lightgreen')
axs[0, 1].set_title('Top 5 Artists in the 00s', fontsize=14)
axs[0, 1].invert_yaxis()

# 10年代
axs[1, 0].barh(top_artists_10s.index, top_artists_10s.values, color='lightcoral')
axs[1, 0].set_title('Top 5 Artists in the 10s', fontsize=14)
axs[1, 0].invert_yaxis()

# 所有时间段
axs[1, 1].barh(top_artists_all_time.index, top_artists_all_time.values, color='gold')
axs[1, 1].set_title('Top 5 Artists of All Time', fontsize=14)
axs[1, 1].invert_yaxis()

for ax in axs.flat:
    ax.set_xlabel('Number of Albums in Top 100', fontsize=12)
plt.tight_layout(pad=2.5, h_pad=4.0, w_pad=2.5)  # pad 控制整体间距，h_pad 控制子图之间的垂直间距
 # hspace 控制行间距，默认是0.2，增大它可以增加行间距


# plt.tight_layout()
plt.show()
