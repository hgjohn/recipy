import requests
import json

url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"

querystring = {"ingr":"apple"}# "ingr":"banana"}

headers = {
	"X-RapidAPI-Key": "66c11ad3c1mshcab242ab4c9a6abp19ed96jsne88329d755ee",
	"X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
 
nutrients = response.text.find("nutrients")
end_nutrients = response.text.find('}')
nutrient_dict = json.loads(response.text[nutrients+11:end_nutrients+1])
print(nutrient_dict)