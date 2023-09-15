import requests
import toml
import email_notif
import re
import time

config = toml.load('config.toml')
items = config['items']
store_id = config['user']['store_id']
headers = {
    'Host': 'www.microcenter.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.microcenter.com/search',
    'Accept-Language': 'en-US,en;q=0.9',
}

items_availability = {}
delay_between_items = 1

for item in items:
    item_name = item['name']
    item_url = item['url'] + store_id

    response = requests.get(item_url, headers=headers)
    availability = response.text

    if 'https://schema.org/Instock' in availability:
        inventory_pattern = r'<span class="inventoryCnt">(\d+)\s*<span class="msgInStock">NEW IN STOCK</span></span>'

        match = re.search(inventory_pattern, availability)

        availability_status = "In stock!"
        inventory_count = match.group(1) if match else "N/A"

        print(f"{availability_status} : {item_name} : {inventory_count} available")

        items_availability[item_name] = {
            'availability_status': availability_status,
            'inventory_count': inventory_count
        }
    elif 'https://schema.org/Outofstock' in availability:
        availability_status = "Sold out"
        print(f"{availability_status} : {item_name}")
        items_availability[item_name] = {
            'availability_status': availability_status,
            'inventory_count': "N/A"
        }
    else:
        availability_status = "error"
        print(f"Error checking inventory for {item_name}: {response.text}")
        items_availability[item_name] = {
            'availability_status': availability_status,
            'inventory_count': "N/A"
        }

    time.sleep(delay_between_items)

if items_availability:
    email_notif.send_notification(items_availability)

if items_availability:
    email_notif.send_notification(items_availability)
