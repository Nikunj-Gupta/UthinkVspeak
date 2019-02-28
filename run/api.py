import unirest 
import os 

text = "Know" 
link = "https://viomatic-com-text-to-speech-tts-v1.p.rapidapi.com/getmp3?sex=female&text="+text+"&language=en"
response = unirest.post(link,
  headers={
    "X-RapidAPI-Key": "7ho01z1QfEmshzZStpsoSd4lSP8ip1IylWwjsnaEcBFQqOePxE",
    "Content-Type": "application/x-www-form-urlencoded"
  }
)


lk = str(response.body['file']) 
lk = 'wget ' + lk 
os.system(lk) 