import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def process_file(filename):
    decade = filename[7:10]
    country = filename[11:13].upper()
    df = pd.read_csv(filename)
    avg_rating = df['Rating'].mean()
    avg_num_ratings = df['Number of Rating'].mean()
    return decade, country, avg_rating, avg_num_ratings


def main():
    data = []
    for file in os.listdir():
        if file.startswith('top') and file.endswith('.csv'):
            data.append(process_file(file))

    df = pd.DataFrame(data, columns=['Decade', 'Country', 'Avg Rating', 'Avg Number of Ratings'])

    # Pivot the data for easier plotting
    df_rating = df.pivot(index='Decade', columns='Country', values='Avg Rating')
    df_num_ratings = df.pivot(index='Decade', columns='Country', values='Avg Number of Ratings')

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 16))

    # Plot average ratings
    sns.heatmap(df_rating, annot=True, cmap='YlOrRd', ax=ax1)
    ax1.set_title('Average Album Rating by Country and Decade')

    # Plot average number of ratings
    sns.heatmap(df_num_ratings, annot=True, cmap='YlGnBu', ax=ax2)
    ax2.set_title('Average Number of Ratings by Country and Decade')

    plt.tight_layout()
    plt.savefig('album_ratings_analysis.png')
    print("Analysis complete. Chart saved as 'album_ratings_analysis.png'.")


if __name__ == "__main__":
    main()