import toml
import yagmail

def send_notification(items_availability):
    config = toml.load('config.toml')
    user = config['user']['email_sender']
    sender_password = config['user']['sender_password']
    email_receiver = config['user']['email_receiver']
    
    yag = yagmail.SMTP(user=user, password=sender_password)
    subject = "Product Availability Notification"
    body = ""
    for item_name, availability_info in items_availability.items():
        availability_status = availability_info['availability_status']
        inventory_count = availability_info['inventory_count']
        
        if availability_status == "In stock!":
            body += f"{availability_status} : {item_name} : {inventory_count} available\n"
        else:
            body += f"{availability_status} : {item_name}\n"
    
    yag.send(to=email_receiver, subject=subject, contents=body)
    print("Sent notification")
