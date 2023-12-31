import requests
import pandas as pd
import json
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

from_data = os.getenv('FROM_DATA')
to_data = os.getenv('TO_DATA')
access_token = os.getenv('ACCESS_TOKEN')
URL = os.getenv('URL')


url = f'{URL}/posts?fields=id,message,created_time&since={from_data}&until={to_data}&access_token={access_token}'

response = requests.get(url)

data = json.loads(response.text)


def save_json(data, file):
    with open(file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)

def save_csv(data, file):
    # Convert the list to a DataFrame
    df = pd.DataFrame(data)
    # Save the DataFrame to an CSV file
    df.to_csv(file, index=False)


def get_next_page(current_json_data):
    if 'paging' in current_json_data and 'next' in current_json_data['paging']:

        next_page_url = current_json_data['paging']['next']  

        # Make a request to the next page URL
        response = requests.get(next_page_url)

        if response.status_code == 200:
            # Parse the JSON data from the response
            next_page_data = response.json()

            # Update the current JSON data with the new page data
            current_json_data["data"].extend(next_page_data["data"])

            # Update the "paging" information with the next page's cursors
            current_json_data["paging"] = next_page_data.get("paging", {})

            return current_json_data
        else:
            print(f"Error fetching next page. Status code: {response.status_code}")
            return None  

# Check if the response contains 'data' key
if 'data' in data:
    posts = data['data']

    extracted_data_list = []

    # Define a function to extract values from a post and append to the list
    def extract_values(post):
        post_id = post.get('id', '')
        message = post.get('message', '')
        created_time = post.get('created_time', '')
        
        # Append extracted values to the list
        extracted_data_list.append({'post_id': post_id, 'message': message, 'created_time': created_time})

    # Use map to apply the function to each post
    _ = list(map(extract_values, posts))

        # Check if there are more pages
    while 'paging' in data and 'next' in data['paging']:
        # Fetch the next page
        data = get_next_page(data)

        # Check if the response contains 'data' key
        if 'data' in data:
            posts = data['data']

            # Use map to apply the function to each post
            _ = list(map(extract_values, posts))
        else:
            print("No data found in the response.")
    

    json_file = 'extracted_data.json'
    csv_file = 'extracted_data.csv'

    save_json(extracted_data_list, json_file)
    save_csv(extracted_data_list, csv_file)


else:
    print("No data found in the response.")
