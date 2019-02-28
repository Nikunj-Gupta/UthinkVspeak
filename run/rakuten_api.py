import unirest 


query = "laptop" 

link = "https://rakuten_webservice-rakuten-recipe-v1.p.rapidapi.com/services/api/Recipe/CategoryList/20170426?callback="+query+"&categoryType=large"

response = unirest.get(link,
  headers={
    "X-Mashape-Key": "7ho01z1QfEmshzZStpsoSd4lSP8ip1IylWwjsnaEcBFQqOePxE",
    "X-Mashape-Host": "rakuten_webservice-rakuten-recipe-v1.p.rapidapi.com"
  }
)

lk = response.body 
#print lk 

import json 
lk2 = lk[len(query)+1:-2] 
d = json.loads(lk2) 



for i in d['result']['large']: 
	print i['categoryId'], " " , 