import json
import requests

# Make API request
response = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?apikey=Skl0KMwYVc7suTtyYkxqUJPR1S37dtB2")

# Convert response to JSON format
data = response.json()

# Store data in JSON file
with open("data.json", "w") as outfile:
    json.dump(data, outfile)