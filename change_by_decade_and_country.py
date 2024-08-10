import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def process_file(filename):
    decade = filename[7:10]
    country = filename[11:13].upper()
    if country == 'JA':
        country = 'Japan'
    if country == 'FR':
        country = 'France'
    if country == 'SK':
        country = 'South Korea'
    if country == 'UK':
        country = 'United Kingdom'
    if country == 'US':
        country = 'United States'
    if country == 'GE':
        country = 'Germany'
    df = pd.read_csv(filename)
    avg_rating = df['Rating'].mean()
    avg_num_ratings = df['Number of Rating'].mean()
    return decade, country, avg_rating, avg_num_ratings


def main():
    sns.set(style="ticks")
    palette = sns.color_palette("husl", 6)  # 设置调色板

    data = []
    for file in os.listdir():
        if file.startswith('top') and file.endswith('.csv'):
            data.append(process_file(file))

    df = pd.DataFrame(data, columns=['Decade', 'Country', 'Avg Rating', 'Avg Number of Ratings'])

    # Sort the dataframe by decade to ensure correct order in the plot
    df['Decade'] = pd.Categorical(df['Decade'], categories=['90s', '00s', '10s'], ordered=True)
    df = df.sort_values('Decade')

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 16))

    # Plot average ratings
    for i, country in enumerate(df['Country'].unique()):
        country_data = df[df['Country'] == country]
        ax1.plot(country_data['Decade'], country_data['Avg Rating'], marker='o', label=country,
                 color=palette[i], linestyle='-')

    ax1.set_title('Average Album Rating by Country and Decade', fontsize=18)
    ax1.set_xlabel('Decade', fontsize=16)
    ax1.set_ylabel('Average Rating', fontsize=16)
    ax1.legend(fontsize=12, loc='best')
    ax1.tick_params(axis='both', which='major', labelsize=14,direction='in', length=6, width=1)
    ax1.grid(False)  # Cancel gridlines

    # Plot average number of ratings
    for i, country in enumerate(df['Country'].unique()):
        country_data = df[df['Country'] == country]
        ax2.plot(country_data['Decade'], country_data['Avg Number of Ratings'], marker='o', label=country,
                 color=palette[i], linestyle='-')
        # for j in range(len(country_data)):
        #     ax2.text(country_data['Decade'].iloc[j], country_data['Avg Number of Ratings'].iloc[j],
        #              f'{country_data["Avg Number of Ratings"].iloc[j]:.2f}', ha='center', va='bottom', fontsize=10)

    ax2.set_title('Average Number of Ratings by Country and Decade', fontsize=18)
    ax2.set_xlabel('Decade', fontsize=16)
    ax2.set_ylabel('Average Number of Ratings', fontsize=16)
    ax2.legend(fontsize=13, loc='best')
    ax2.tick_params(axis='both', which='major', labelsize=14,direction='in', length=6, width=1)
    ax2.grid(False)  # Cancel gridlines

    plt.tight_layout()

    plt.savefig('album_ratings_analysis.png')
    print("Analysis complete. Improved chart saved as 'album_ratings_analysis.png'.")
    plt.show()

if __name__ == "__main__":
    main()
