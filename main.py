from ticket_master import TicketMasterAPI
# ticket master data
base_url = "https://app.ticketmaster.com/discovery/v2/events.json"
api_key = "Skl0KMwYVc7suTtyYkxqUJPR1S37dtB2"
# google sheet manager data
credentials_file = 'fleet-joy-392518-26ce6cb44572.json'
sheet_name = 'Ticket master sheet'

tm_api = TicketMasterAPI(base_url, api_key, credentials_file, sheet_name, 10)
tm_api.get_all_data()
