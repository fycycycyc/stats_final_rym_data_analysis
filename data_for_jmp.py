import pandas as pd

# 加载数据
data_90s = pd.read_csv('top100_90s_ja.csv')
data_00s = pd.read_csv('top100_00s_ja.csv')
data_10s = pd.read_csv('top100_10s_ja.csv')

# 添加 decade 列
data_90s['Decade'] = '90s'
data_00s['Decade'] = '00s'
data_10s['Decade'] = '10s'

# 提取 rating 和 number of rating 列，并添加 decade 列
data_90s_filtered = data_90s[['Decade', 'Rating', 'Number of Rating']]
data_00s_filtered = data_00s[['Decade', 'Rating', 'Number of Rating']]
data_10s_filtered = data_10s[['Decade', 'Rating', 'Number of Rating']]

# 合并数据
combined_data = pd.concat([data_90s_filtered, data_00s_filtered, data_10s_filtered])

# 保存为新的CSV文件
combined_data.to_csv('for_jmp.csv', index=False)
