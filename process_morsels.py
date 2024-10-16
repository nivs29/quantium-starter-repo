import pandas as pd
import os

data_folder = 'data/'
csv_files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']
dataframes = []

for file in csv_files:
    df = pd.read_csv(os.path.join(data_folder, file))
    df = df[df['product'] == 'pink morsel']
    df['sales'] = df['quantity'] * df['price']
    df =  df[['sales', 'date', 'region']]
    dataframes.append(df)

final_df = pd.concat(dataframes)
output_file = 'formatted_output.csv'
final_df.to_csv(output_file, index=False)
print(f"Data has been processed and saved to {output_file}")
