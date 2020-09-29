import pandas as pd
import argparse
import os

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('--land_data')
argument_parser.add_argument('--area_of_interest')
args = argument_parser.parse_args()

area_interest = pd.read_csv(f'./{args.area_of_interest}')
land_price = pd.read_csv(f'./{args.land_data}')
land_price.columns = ['TransactionID', 'Price', 'Date', 'Postcode', 'PropertyType', 'NewlyBuilt', 'Duration', 'PAON', 'SAON', 'Street', 'Locality', 'City', 'District', 'County', 'PPD', 'RecordStatus']
# Remove unused columns
land_price = land_price[['TransactionID', 'Price', 'Postcode', 'District']]

def filter_by_text(df, col, val):
    series = df[col]
    filtered_df = df[df[col] == val.upper()]
    return filtered_df

def filter_by_text_start(df, col, val):
    series = df[col]
    filtered_df = df.loc[series.str.startswith(val, na=False)]
    return filtered_df

unique_areas = area_interest['area_name'].unique()
output = []

for area in unique_areas:
    total_area_price = 0
    postcodes = area_interest[area_interest['area_name'] == area]['sector']
    # Filter by area to reduce num_records
    area_price = land_price.pipe(filter_by_text, 'District', area)
    for p in postcodes:
        sector_price = area_price.pipe(filter_by_text_start, 'Postcode', p)
        total_sector_price = sector_price['Price'].sum()

        total_area_price += total_sector_price

    output.append([area, total_area_price])

output = pd.DataFrame(output, columns=['Area', 'MarketValue'])

if not os.path.exists('./output'): os.mkdir('output')
output.to_csv('./output/area_value.csv', index=False)