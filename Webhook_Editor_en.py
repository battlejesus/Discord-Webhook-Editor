import os
import time
import requests
from colorama import Fore, init

os.system("title Webhook Editor")

def single(webhook_url, message, username_choice):
    data = {
        "content": message,
        "username": username_choice
    }
    
    result = requests.post(webhook_url, json=data)
    
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

def spam(webhook_url, message, interval, count, username_choice):
    data = {
        "content": message,
        "username": username_choice
    }
    
    if count == 0:
        while True:
            result = requests.post(webhook_url, json=data)
            
            try:
                result.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print(f"HTTP error occurred: {err}")
            else:
                print("Payload delivered successfully, code {}.".format(result.status_code))
            
            time.sleep(interval)
    else:
        for _ in range(count):
            result = requests.post(webhook_url, json=data)
            
            try:
                result.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print(f"HTTP error occurred: {err}")
            else:
                print("Payload delivered successfully, code {}.".format(result.status_code))
            
            time.sleep(interval)

def delete(webhook_url):
    response = requests.delete(webhook_url)
    # Sonuçları kontrol etme
    if response.status_code == 204:
        print("Webhook Deleted Successfully")
    else:
        print(f"Webhook deletion failed. HTTP Status Code: {response.status_code}")

init(autoreset=True)
print(Fore.RED + """ █     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒ 
▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░ 
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄ 
░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒
  ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░
  ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░ 
    ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░   
                      ░                                  
▓█████ ▓█████▄  ██▓▄▄▄█████▓ ▒█████   ██▀███             
▓█   ▀ ▒██▀ ██▌▓██▒▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒           
▒███   ░██   █▌▒██▒▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒           
▒▓█  ▄ ░▓█▄   ▌░██░░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄             
░▒████▒░▒████▓ ░██░  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒           
░░ ▒░ ░ ▒▒▓  ▒ ░▓    ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░           
 ░ ░  ░ ░ ▒  ▒  ▒ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░           
   ░    ░ ░  ░  ▒ ░  ░      ░ ░ ░ ▒    ░░   ░            
   ░  ░   ░     ░               ░ ░     ░                
        ░                                                """)
print(Fore.BLUE + "By BattleJesus")
menu = """\nWhat You Want?
    1 - Webhook Message Sender (Single)
    2 - Webhook Message Sender (Spam)
    3 - Webhook Deleter (You can delete webhooks)
"""

print(menu)

select = input()
if select == "1":
    print("You Selected Webhook Message Sender (Single)")
    webhook_url = input("Enter Your Webhook URL: ")
    username_choice = input("What's the webhook username?")
    message = input("What is your message?: ")
    single(webhook_url, message, username_choice)

elif select == "2":
    print("You Selected Webhook Message Sender (Spam)")
    webhook_url = input("Enter Your Webhook URL: ")
    username_choice = input("What's the webhook username?")
    message = input("What is your message?: ")
    interval = float(input("Enter interval between messages (seconds): "))
    count = int(input("Enter number of messages to send (0 for infinite): "))
    spam(webhook_url, message, interval, count, username_choice)

elif select == "3":
    print("You Selected Webhook Deleter")
    webhook_url = input("Enter Your Webhook URL: ")
    delete(webhook_url)

else:
    print("Wrong Choice")