import requests
import time
from colorama import *
from notifier import notify
from domains import urls
import os 

os.system("cls" if os.name == "nt" else "clear")

with open("../webhook.txt", "r", encoding="utf-8") as file:
    for line in file:
        webhook = line.strip()

try:
    for url in urls:
        start = time.time()
        response = requests.get(url)
        end = time.time()
        res_time = end - start    
        send = f"```[INFO] | {url} STATUS: {response.status_code} |  TIME: {res_time}```"
        print(f"[{Back.GREEN}INFO{Style.RESET_ALL}] {url}: UP | TIME: {res_time}")
        notify(send, webhook)  
    input()

except ConnectionError:
    print("[!] Connection error: The website has recused the connection.")
    input()
except KeyboardInterrupt:
    exit()
except OSError as e:
    print(f"[!] Unknown error: {e}")



