import requests
import pandas as pd
import json

from_data = '2019-01-01' 
to_data = '2023-11-15' 
access_token = 'EAAFFqzOZCkaYBO0kOXbmPwsfmut80NonBRxQiYzDfEeWE5ZBosa73vHUTC0XbORBxZACRZBtMozQdXnzXJi5F3GkbDbDlphyg7CZBvA1oOAlhPTW2vHRme2MUKQwyzDZBxdXFiweYOAZCckI5nqJniNPQa0CbtIrYRpxRaBXlslCyfceu2XZB0aojaaGBIaEENFybe6evLb89ZCGm6bhJZCKk5veAZD'

url = f'https://graph.facebook.com/v18.0/jayantsinhabjp/posts?fields=id,message,created_time&since={from_data}&until={to_data}&access_token={access_token}'

response = requests.get(url)

data = json.loads(response.text)
# Check if the response contains 'data' key
if 'data' in data:
    posts = data['data']

    # Define a function to extract values from a post
    def extract_values(post):
        post_id = post.get('id', '')
        message = post.get('message', '')
        created_time = post.get('created_time', '')
        return {'post_id': post_id, 'message': message, 'created_time': created_time}

    # Use map to apply the function to each post
    mapped_data = list(map(extract_values, posts))
    
    # Print the mapped data
    for post_data in mapped_data:
        print(post_data)

    # Convert the mapped data to a DataFrame
    df = pd.DataFrame(mapped_data)

    # Save the DataFrame to an Excel file
    df.to_excel('posts.xlsx', index=False)
else:
    print("No data found in the response.")
