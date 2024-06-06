import os
import time
import requests
from colorama import Fore, init

os.system("title Webhook Düzenleyici")

def single(webhook_url, message, username_choice):
    data = {
        "content": message,
        "username": username_choice
    }
    
    result = requests.post(webhook_url, json=data)
    
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP hatası oluştu: {err}")
    else:
        print("Mesaj başarıyla teslim edildi, HTTP Durum Kodu  {}.".format(result.status_code))

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
                print("Mesaj başarıyla teslim edildi, HTTP Durum Kodu  {}.".format(result.status_code))
            
            time.sleep(interval)
    else:
        for _ in range(count):
            result = requests.post(webhook_url, json=data)
            
            try:
                result.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print(f"HTTP hatası oluştu: {err}")
            else:
                print("Mesaj başarıyla teslim edildi, HTTP Durum Kodu {}.".format(result.status_code))
            
            time.sleep(interval)

def delete(webhook_url):
    response = requests.delete(webhook_url)
    # Sonuçları kontrol etme
    if response.status_code == 204:
        print("Webhook başarıyla silindi")
    else:
        print(f"Webhook silme çalışmadı. HTTP Durum Kodu: {response.status_code}")

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
print(Fore.BLUE + "BattleJesus Tarafından")
menu = """\nWhat You Want?
    1 - Webhook Message Gönderici (Single)
    2 - Webhook Message Gönderici (Spam)
    3 - Webhook Silici (Webhook'ları silebilirsin.)
"""

print(menu)

select = input()
if select == "1":
    print("Webhook Mesajı Göndericisini Seçtiniz (Single)")
    webhook_url = input("Webhook URL'nizi girin: ")
    username_choice = input("Webhook'un kullanıcı adı ne olsun?")
    message = input("Mesajın Ne?: ")
    single(webhook_url, message, username_choice)

elif select == "2":
    print("Webhook Mesajı Göndericisini Seçtiniz (Spam)")
    webhook_url = input("Webhook URL'nizi girin: ")
    username_choice = input("Webhook'un kullanıcı adı ne olsun?")
    message = input("Mesajın Ne?: ")
    interval = float(input("Mesajların kaç saniye aralıklarla gönderileceğini girin: "))
    count = int(input("Kaç tane mesaj gönderileceğini girin (Sonsuz için '0'): "))
    spam(webhook_url, message, interval, count, username_choice)

elif select == "3":
    print("Webhook Silici'yi Seçtin")
    webhook_url = input("Webhook URL'nizi girin: ")
    delete(webhook_url)

else:
    print("Yanlış Seçim")