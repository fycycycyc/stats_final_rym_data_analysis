import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def process_file(filename):
    decade = filename.split('_')[1][:3]
    df = pd.read_csv(filename)
    avg_rating = df['Rating'].mean()
    avg_num_ratings = df['Number of Rating'].mean()
    return decade, avg_rating, avg_num_ratings

def main():
    files = [
        'top100_90s_ja.csv',
        'top100_00s_ja.csv',
        'top100_10s_ja.csv'
    ]

    data = [process_file(file) for file in files]
    df = pd.DataFrame(data, columns=['Decade', 'Avg Rating', 'Avg Number of Ratings'])
    df['Decade'] = pd.Categorical(df['Decade'], categories=['90s', '00s', '10s'], ordered=True)
    df.sort_values('Decade', inplace=True)

    sns.set(style="ticks")  # 使用纯白风格
    palette = sns.color_palette("husl", 10)  # 设置调色板

    plt.figure(figsize=(10,12))  # 设置整体图形大小

    # Plot for average ratings
    plt.subplot(2, 1, 1)  # 定义子图
    plt.plot(df['Decade'], df['Avg Rating'], marker='o', linestyle='-', color=palette[3], markersize=8, linewidth=2)
    plt.title('Average Album Rating by Decade in Japan', fontsize=18)
    plt.xlabel('Decade', fontsize=16)
    plt.ylabel('Average Rating', fontsize=16)
    # plt.xticks(fontsize=12)  # 增大刻度大小
    # plt.yticks(fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=14, direction='in', length=6, width=1)

    # Plot for average number of ratings
    plt.subplot(2, 1, 2)  # 定义子图
    plt.plot(df['Decade'], df['Avg Number of Ratings'], marker='o', linestyle='-', color=palette[2], markersize=8, linewidth=2)
    plt.title('Average Number of Ratings by Decade in Japan', fontsize=18)
    plt.xlabel('Decade', fontsize=16)
    plt.ylabel('Average Number of Ratings', fontsize=16)
    # plt.xticks(fontsize=14)  # 增大刻度大小
    # plt.yticks(fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14, direction='in', length=6, width=1)

    plt.tight_layout()  # 优化布局
    plt.savefig('trend_album_ratings_analysis_japan.png', dpi=600)  # 保存为高分辨率
    plt.show()

if __name__ == "__main__":
    main()
