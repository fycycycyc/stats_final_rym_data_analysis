import pandas as pd

# Load the CSV file
file_path = 'top100_00s_sk.csv'
df = pd.read_csv(file_path)

# Rename the first column to "Rank" if it's not already named so
if df.columns[0] != 'Rank':
    df.rename(columns={df.columns[0]: 'Rank'}, inplace=True)

# Change the 'Rank' column to ascending order from 1 to 100
df['Rank'] = range(1, 101)

# Save the modified dataframe to a new CSV file
output_file_path = 'top100_00s_sk.csv'
df.to_csv(output_file_path, index=False)

# Optional: Display the first few rows of the modified dataframe
print(df.head())
