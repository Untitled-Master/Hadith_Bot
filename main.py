from flask import Flask
from threading import Thread
import facebook
import requests
import random
import time

#hosting
app = Flask('')


@app.route('/')
def home():
  return "Lina Api"


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()


keep_alive()

access_token = 'EAAWGa1uBPLsBO2mjOIPYyaVtBcZCM2dm7iqJCcplr3TnpC2Fjob6yiIqDMRL8JmZC8kUrTk83vwpzsnE06ZAXtAi3xzPIkP4ujg6QDiTZC1w1ZBEGBEHGiISZBmXRHLIgK2TwBClmw2Ba8hmR3PZBm7VPUDA9sdytefD4oXbA6GrAoTsXiZAQwk8OgZBNJCcQx8xZAYLtJYieD7q0mWDoZASHuwvZBZAk8QZDZD'
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

