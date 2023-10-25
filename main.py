from ticket_master import TicketMasterAPI
from google_sheet_manager import GoogleSheetManager
# get data
base_url = "https://app.ticketmaster.com/discovery/v2/events.json"
api_key = "Skl0KMwYVc7suTtyYkxqUJPR1S37dtB2"

tm_api = TicketMasterAPI(base_url, api_key)
all_data = tm_api.get_all_data()


# insert data
credentials_file = 'fleet-joy-392518-26ce6cb44572.json'
sheet_name = 'Ticket master sheet'

# Initialize the GoogleSheetManager object
manager = GoogleSheetManager(credentials_file, sheet_name)

# Call the insert_data method multiple times
for record in all_data:
    manager.insert_data(record)