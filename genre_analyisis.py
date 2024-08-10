from pickle import FALSE

import pandas as pd
import matplotlib.pyplot as plt

# 加载数据
data_90s = pd.read_csv('top100_90s_ja.csv')
data_00s = pd.read_csv('top100_00s_ja.csv')
data_10s = pd.read_csv('top100_10s_ja.csv')

data_90s['Decade'] = '90s'
data_00s['Decade'] = '00s'
data_10s['Decade'] = '10s'

# 合并数据
combined_data = pd.concat([data_90s, data_00s, data_10s])

# 分离流派数据，并展开成单独的行
combined_data['Genre'] = combined_data['Genre'].str.split(',')
genres_exploded = combined_data.explode('Genre')

# 去除可能存在的前后空格，并统计每个年代中流派的出现次数
genres_exploded['Genre'] = genres_exploded['Genre'].str.strip()
genre_count = genres_exploded.groupby(['Decade', 'Genre']).size().unstack(fill_value=0)

# 对每个年代选择最常见的前10个流派
top_genres_90s = genre_count.loc['90s'].sort_values(ascending=False).head(10)
top_genres_00s = genre_count.loc['00s'].sort_values(ascending=False).head(10)
top_genres_10s = genre_count.loc['10s'].sort_values(ascending=False).head(10)

# 绘制柱状图
fig, axs = plt.subplots(3, 1, figsize=(10, 18))

axs[0].barh(top_genres_90s.index, top_genres_90s.values, color='skyblue')
axs[0].set_title('Top 10 Genres in the 90s')
axs[0].invert_yaxis()  # Invert y-axis to have the highest on top

axs[1].barh(top_genres_00s.index, top_genres_00s.values, color='lightgreen')
axs[1].set_title('Top 10 Genres in the 00s')
axs[1].invert_yaxis()

axs[2].barh(top_genres_10s.index, top_genres_10s.values, color='lightcoral')
axs[2].set_title('Top 10 Genres in the 10s')
axs[2].invert_yaxis()

for ax in axs:
    ax.set_xlabel('Number of Albums')

plt.tight_layout()
plt.show()
