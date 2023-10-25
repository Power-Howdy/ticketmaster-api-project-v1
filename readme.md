# TicketMaster Free API and Google Sheet

This project is a python script that gets data from ticket master free api and adds it to the google sheet.

## Requirements

- Python 3.10.11
- Google API Credentials
- Ticket Master API

## How to use this script


### Register on Ticket Master and get API

- https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/
- set the api key in the **settings.py** file

### Set up your Google Sheets API credentials: 

- Go to the Google Cloud Console (https://console.cloud.google.com/). 
- Create a new project or select an existing one. 
- Enable the Google Sheets API for your project. 
- Create credentials (OAuth client ID) and download the JSON file containing the credentials. 
- Set the "credentials_file" value in **settings.py**

### Granting Access to Google Sheets

- Open the Google Sheet you want to grant access to. 
- Click on the "Share" button in the top-right corner of the Google Sheet. 
- In the "Share with others" dialog box, enter the service account email address in the "People" field. 
- Set the appropriate access level for the service account (e.g., Viewer, Editor, or Owner) using the drop-down menu. 
- Click on the "Send" button to grant access to the service account. 
- The service account email address will now have access to the Google Sheet, allowing you to work with it using the Python script. 
- Set the Google Sheet name in the **settings.py** file.


### Installation
- Creating virtual environment

```bash
 python -m venv 'path_to_directory'
```

- Installing libraries

```bash
pip install -r requirements.txt
```


### Run the script

```bash
py main.py
```
