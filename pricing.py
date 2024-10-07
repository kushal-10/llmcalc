import pandas as pd  
import requests
import os

def fetch_prices():
    # Fetch the JSON data from the URL
    url = "https://llm-price.huhuhang.workers.dev/"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Extract relevant information
        extracted_data = []
        for entry in data:
            extracted_info = {
                "model_name": entry["fields"]["model_name"],
                "provider": entry["fields"]["provider"],
                "input_tokens": entry["fields"]["input_tokens"],
                "output_tokens": entry["fields"]["output_tokens"],
                "url": entry["fields"]["url"],
                "update_time": entry["fields"]["update_time"]
            }
            extracted_data.append(extracted_info)

        # Create a DataFrame from the extracted data
        df = pd.DataFrame(extracted_data)
        if not os.path.exists('data'):
            os.makedirs('data')
        save_path = os.path.join('data', 'prices.csv')
        df.to_csv(save_path, index=False)  # Save the DataFrame as a CSV file
        print(f"Saved the Prices as a CSV under {save_path}")
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None  
    
if __name__ == '__main__':
    fetch_prices()
    