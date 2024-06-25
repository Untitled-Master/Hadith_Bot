from flask import Flask
from threading import Thread
import facebook
import requests
import random
import time

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()


access_token = 'EAAWGa1uBPLsBOZCNdW8h3xuwrvqMi0pncleQzXDbRTL2Ou5ZBvykgfLHJMF2VzXE5nHqWJA9Px6wnZBL9I83qD0yuSRagjhATtZCHYZBPX9HU9TokvZBOZCGTsgPhV2TXWMBauAm48iEiiqAyZCRMP8Wb7EL6MS3MyiuELZCw4ZAZCS2rbpZANjgZBvfzDaLkXsVpcaxeWqht7ZBqCRxdGKKjnjMZBEvKuO'
# Connection to the Facebook API
graph = facebook.GraphAPI(access_token)
image = requests.get("https://i.pinimg.com/originals/ee/aa/76/eeaa7609f09f9074dd404dba663665d5.jpg").content

n = random.randint(0, 332)
url = f"https://hadis-api-id.vercel.app/hadith/bukhari?page={n}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    hadiths = data["items"]
    
    # Select a random hadith from the list
    random_hadith = random.choice(hadiths)
    
    # Extract the Arabic text and hadith number
    arabic_text = random_hadith["arab"]
    hadith_number = random_hadith["number"]
    text = f"{arabic_text} \n\n\n   [📚 صحيح البخاري] [{n}\{hadith_number}]"
    print(text)
    
    graph.put_photo(message=text, image=image)
    time.sleep(1800)  # Wait for 30 minutes (1800 seconds)
else:
    print('Request failed with status code:', response.status_code)

