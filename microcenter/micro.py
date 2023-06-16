import requests
import toml
import email_notif

config = toml.load('config.toml')
items = config['items']
store_id = config['user']['store_id']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

items_availability = {}

for item in items:
    item_name = item['name']
    item_url = item['url'] + store_id

    response = requests.get(item_url, headers=headers)
    availability = response.text

    if 'https://schema.org/Outofstock' in availability:
        availability_status = "currently out of stock"
    elif 'https://schema.org/Instock' in availability:
        availability_status = "in stock"
    else:
        availability_status = "error"

    print(f"{item_name}: {availability_status}")
    items_availability[item_name] = availability_status

if items_availability:
    email_notif.send_notification(items_availability)
