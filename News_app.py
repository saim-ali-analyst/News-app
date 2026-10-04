# ==========================================
#   Saim News App
#   Author: Saim Ali
#   Description: A simple CLI news reader using NewsAPI
# ==========================================

import requests
import time

def sleep():
    time.sleep(5)

print('==================== Welcome to the Saim News App =====================')

name = input('What is your name? ')

print('========== News Categories ==========')
print('1, General news')
print('2, Sports news')
print('3, Political news')

user = int(input('Please select your category (1/2/3): '))

# ---------- API Config ----------
url = "https://newsapi.org/v2/top-headlines"
my_api = "YOUR_API_KEY_HERE"   # ← paste your NewsAPI key here

if user == 1:
    print(f'\nWelcome to General News, {name}\n')
    para = {
        'country': 'us',
        'category': 'general',
        'apikey': my_api
    }

    response = requests.get(url, params=para)
    print('Status:', response.status_code)

    if response.status_code == 200:
        news = response.json()['articles']
        c = 1
        for article in news:
            print(f"--- News {c} ---")
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print()
            c += 1
            sleep()
    else:
        print('Error fetching news.')

elif user == 2:
    print(f'\nWelcome to Sports News, {name}\n')
    para = {
        'country': 'us',
        'category': 'sports',
        'apikey': my_api
    }

    response = requests.get(url, params=para)
    print('Status:', response.status_code)

    if response.status_code == 200:
        news = response.json()['articles']
        c = 1
        for article in news:
            print(f"--- News {c} ---")
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print()
            c += 1
            sleep()
    else:
        print('Error fetching news.')

elif user == 3:
    print(f'\nWelcome to Political News, {name}\n')
    para = {
        'country': 'us',
        'category': 'politics',
        'apikey': my_api
    }

    response = requests.get(url, params=para)
    print('Status:', response.status_code)

    if response.status_code == 200:
        news = response.json()['articles']
        c = 1
        for article in news:
            print(f"--- News {c} ---")
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print()
            c += 1
            sleep()
    else:
        print('Error fetching news.')

else:
    print('Invalid option. Please select 1, 2, or 3.')