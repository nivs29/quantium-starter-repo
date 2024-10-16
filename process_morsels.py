import pandas as pd
import os

# Define the folder containing the CSV files
data_folder = 'data/'
csv_files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']
dataframes = []

for file in csv_files:
    # Read each CSV file
    df = pd.read_csv(os.path.join(data_folder, file))

    # Filter for only 'pink morsel' products
    df = df[df['product'].str.lower() == 'pink morsel']

    # Calculate sales
    df['sales'] = df['quantity'] * df['price']

    # Select relevant columns and rename them if needed
    df = df[['sales', 'date', 'region']]

    # Append the DataFrame to the list
    dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
final_df = pd.concat(dataframes)

# Convert the 'date' column to datetime format
final_df['date'] = pd.to_datetime(final_df['date'], errors='coerce')

# Remove any rows with NaT in the 'date' column (if any)
final_df = final_df.dropna(subset=['date'])

# Remove duplicates if necessary
final_df = final_df.drop_duplicates()

# Sort the DataFrame by date
final_df = final_df.sort_values(by='date')

# Save the final DataFrame to a CSV file
output_file = 'formatted_output.csv'
final_df.to_csv(output_file, index=False)

print(f"Data has been processed and saved to {output_file}")

