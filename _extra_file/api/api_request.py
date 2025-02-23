import requests
import json
# {
#   "event_name": "Southend Utd - Barnet",
#   "bet_choice": "Under 2.5",
#   "bet_odds": "2.10",
#   "name": "forebet"
# },
# responses = requests.get("https://api.apify.com/v2/datasets/b1Ht0rfpOD0BNWkDg/items?token=apify_api_rG2EyvhSIHzPcMiemGZ0ZNVFUE6jdn0iQgwH")
responses = requests.get("https://api.apify.com/v2/datasets/aBA2ryS6WGANxLabR/items?token=apify_api_C6OAXyjCXlSQvNf82QfdrMXbNFEQRP0M4LCq")
print(responses.status_code)
responses = responses.json()

with open("api/responses.json", "w", encoding="utf-8") as file:
    json.dump(responses, file, ensure_ascii=False, indent=4)
count = 0
data_under_over = []
for response in responses:
    if response["bet_choice"] == "Under 2.5" or response["bet_choice"] == "Over 2.5":
        data_under_over.append(response)
        count = count + 1

with open("api/Over_Under.json", "w", encoding="utf-8") as file:
    json.dump(data_under_over, file, ensure_ascii=False, indent=4)
    
print(count)