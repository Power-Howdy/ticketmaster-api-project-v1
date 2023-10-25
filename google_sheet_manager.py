import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetManager:
    def __init__(self, credentials_file, sheet_name):
        # Set up credentials
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
        self.client = gspread.authorize(credentials)
        
        # Open the Google Sheet
        self.sheet = self.client.open(sheet_name).get_worksheet(0)
    
    def insert_data(self, data):
        # Add data to the sheet
        self.sheet.append_row(data)        

