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
    for item_name, availability_status in items_availability.items():
        body += f"The {item_name} is {availability_status}.\n"
    yag.send(to=email_receiver, subject=subject, contents=body)
    print("Sent notification")
