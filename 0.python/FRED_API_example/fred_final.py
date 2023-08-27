import requests
import pandas as pd
import json

# Initialize your API key and base URL
with open('secret_key.json') as f:
    secrets = json.loads(f.read())
    
API_KEY = secrets['FRED_API_KEY']

# Initialize your API key and base URL
BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

# List of series to fetch
series_list = ['DGS1MO', 'DGS3MO', 'DGS6MO', 'DGS1', 'DGS2', 'DGS3', 'DGS7']

# Initialize an empty DataFrame to store the final data and metadata
final_df = pd.DataFrame()

# Loop through each series ID to fetch data
for series_id in series_list:
    # Build the API request URL
    data_url = f"{BASE_URL}?series_id={series_id}&api_key={API_KEY}&file_type=json&units=lin&frequency=m&observation_start=2001-07-31"
    
    # Make the API request and parse the JSON response
    response = requests.get(data_url)
    data = response.json()
    
    # Convert the data to a Pandas DataFrame and select only 'date' and 'value'
    df = pd.DataFrame(data['observations'])[['date', 'value']]
    df.columns = ['date', 'value']

    # Extract metadata (assuming metadata is available in the API response)
    series_name = series_id  # Replace with actual metadata
    source = "Source_Here"  # Replace with actual metadata
    release = "Release_Here"  # Replace with actual metadata
    frequency = "Monthly"  # Replace with actual metadata
    date = "Date" # Replace with actual metadata
    
    # Create metadata DataFrame
    metadata_df = pd.DataFrame({
        'date': ['series_name', 'source', 'release', 'frequency', 'date'],
        'value': [series_name, source, release, frequency,'value']
    })


    # Combine metadata and data
    combined_df = pd.concat([metadata_df, df.reset_index(drop=True)])
    print(combined_df)
    
    # Reset the index to avoid empty spaces when concatenating
    combined_df.reset_index(drop=True, inplace=True)
    
    # Add to final DataFrame
    final_df = pd.concat([final_df, combined_df], axis=1)

# Save the data to an Excel file
final_df.to_excel("FRED_Data_final.xlsx", index=False, header=False)