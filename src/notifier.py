import requests
from colorama import *

def notify(send, webhook):
    data = { "content": f"{send}" }
    res = requests.post(webhook, json=data)

    if res.status_code == 204 or 200:
        print(f"[ + ] message sucessfully sent to {Fore.BLUE}Discord{Style.RESET_ALL}")
        print(f"CTRL + C to quit")
    else:
        print(f"[ - ] error while sending message trough {Fore.BLUE}Discord Webhook{Style.RESET_ALL}")
        print(f"[ ! ] status code: {res.status_code}")

