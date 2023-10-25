from ticket_master import TicketMasterAPI
from settings import base_url, api_key, credentials_file, sheet_name, limit

tm_api = TicketMasterAPI(base_url, api_key, credentials_file, sheet_name, limit)
tm_api.get_all_data()
