import requests
import pandas as pd
import json

from_data = '2019-01-01' 
to_data = '2023-11-15' 
access_token = 'EAAFFqzOZCkaYBOzjdCcWPdckArjkxY93P0BRoZA6y69eObPsTpL6DqBX5OaQ8JJfxCXxI3sSdl47CDs1rHmJUv5ZCZCrtgZBcaLHVs4x8KHCmUW7HxuI2qPsM2rZAZBYWCb3rVZCi66rrdBkPQm1CfPmk56liU61EOkZCRmm21JYqBiq4fn0liE2CyogNTozXloEZD'

url = f'https://graph.facebook.com/v18.0/jayantsinhabjp/posts?fields=id,message,created_time&since={from_data}&until={to_data}&access_token={access_token}'

response = requests.get(url)

data = json.loads(response.text)

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
    
    # print(extracted_data_list)
    # Convert the list to a DataFrame
    df = pd.DataFrame(extracted_data_list)

    # Save the DataFrame to an Excel file
    df.to_excel('posts.xlsx', index=False)
else:
    print("No data found in the response.")
