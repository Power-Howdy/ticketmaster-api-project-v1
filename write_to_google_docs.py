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

# Get the URL and ID of the newly created Google Sheet
sheet_url = sheet.url
sheet_id = sheet.id

print("New Google Sheet created successfully!")
print("URL:", sheet_url)
print("ID:", sheet_id)

print("Data added successfully!")