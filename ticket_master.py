import requests
from google_sheet_manager import GoogleSheetManager
class TicketMasterAPI:
    def __init__(self, base_url, api_key, credentials_file, sheet_name, page_limit=0):
        self.base_url = base_url
        self.api_key = api_key
        self.page_size = 20
        self.current_page = 0
        self.total_pages = 1
        self.total_elements = 0
        self.page_limit = page_limit
        # Initialize the GoogleSheetManager object
        self.gsh_manager = GoogleSheetManager(credentials_file, sheet_name)
    def get_data(self):
        url = f"{self.base_url}?apikey={self.api_key}&page={self.current_page}&size={self.page_size}"
        response = requests.get(url)
        data = response.json()
        self.total_pages = data['page']['totalPages']
        self.total_elements = data['page']['totalElements']
        return data['_embedded']['events']
    
    def parse_records(self, data):
        records = []
        for event in data:
            # Parse relevant fields from event and create records
            record = {
                'name': event['name'],
                'date': event['dates']['start']['localDate'],
                'venue': event['_embedded']['venues'][0]['name'],
                # Add more fields as needed
            }
            records.append(record)
        return records
    
    def get_all_data(self):
        # all_records = []
        while self.current_page < self.total_pages:
            print("--> getting data for page ", self.current_page, " of ", self.total_pages)
            if self.page_limit > 0 and self.current_page >= self.page_limit:
              print("--> getting data for page complete as page limit is set: ", self.page_limit)
              break
            else:
              data = self.get_data()
              records = self.parse_records(data)
              self.insert_data_into_google_sheet(records)
              self.current_page += 1
        # return all_records
    def insert_data_into_google_sheet(self, records):
        for record in records:            
          # Extract values dynamically
          result = []
          for key, value in record.items():
              result.append(value)
          self.gsh_manager.insert_data(result)
        