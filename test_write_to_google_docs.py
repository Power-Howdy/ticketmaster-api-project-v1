import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('fleet-joy-392518-26ce6cb44572.json', scope)
client = gspread.authorize(credentials)

# Open the Google Sheet
sheet = client.open('Ticket master sheet').get_worksheet(0)

# Add data to the sheet
data = ['John Doe', 'johndoe@example.com', 'New York']
sheet.append_row(data)

# Get the URL and ID of the Google Sheet
sheet_url = sheet.url

print("Data added to Google Sheet successfully!")
print("URL:", sheet_url)

print("Data added successfully!")