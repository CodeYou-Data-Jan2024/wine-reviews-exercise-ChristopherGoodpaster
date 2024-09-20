# add your code here
import pandas as pd

# Load the dataset
file_path = 'data/winemag-data-130k-v2.csv.zip'
df = pd.read_csv(file_path)

# Group by 'country' and calculate count and mean of points
summary = df.groupby('country').agg(
    count=('country', 'size'),
    points=('points', 'mean')
).reset_index()

# Round the points column to one decimal place
summary['points'] = summary['points'].round(1)

# Save the summary to a new CSV file
output_path = 'data/reviews-per-country.csv'
summary.to_csv(output_path, index=False)

print(f'Summary saved to {output_path}')

