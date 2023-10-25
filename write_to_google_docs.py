import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)

# Open the Google Sheet
sheet = client.open('Test').sheet1

# Add data to the sheet
data = ['John Doe', 'johndoe@example.com', 'New York']
sheet.append_row(data)

print("Data added successfully!")