# Facebook Posts Data Extraction 

## Introduction
This Python script extracts Facebook posts data using the Facebook Graph API. It retrieves posts between a specified date range and saves the extracted data to an Excel file.

### Prerequisites
Before running the script, make sure you have the following:

- Python installed on your machine
- Necessary Python packages installed 
- Facebook Graph API access token
- Install the pandas library

### Getting Started

   1. Clone the UI-Testing branch of this repository:
      ```bash
      git clone https://github.com/TaslimuddinAnsari/swiftchat-scraper.git
      ```

   2. Install the other requirements by running:
      
      Navigate to working directory: 

      ```bash
      cd swiftchat-scraper/
      ```

      Install requirements
      
      ```bash
      pip install -r requirements.txt
      ```
   
   3. Replace the access_token variable with your Facebook Graph API access token.
   4. Set the from_data and to_data variables to define the date range for extracting posts.

### Project Structure
There one folder (swiftchat) and it has a single file- 

- scrap-data.py

### Execute the scrape
    ```bash
    cd swiftchat-scraper/
    ```

   - Navigate to the scraper file
    ```bash
     cd scrap-data/
    ```

   - Run the command
   
    ```bash
     python3 scrap-data.py
    ```
### Script Overview
- The script makes a request to the Facebook Graph API to retrieve posts within the specified date range.
- It handles paginated responses, fetching all available pages of posts.
- Extracted data includes post ID, message, and creation time.
- The data is stored in a Pandas DataFrame and saved to an Excel file (posts.xlsx).

### Note
- Ensure that your Facebook Graph API access token has the necessary permissions to access the required data.
- Depending on the amount of data, the script may take some time to execute.
