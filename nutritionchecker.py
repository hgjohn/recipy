import requests
import json

def fetch_meal():
#user input meal is used to get ingredients dict from themealdb api
#output ingr ran through edamam api to get nutrition dict
    print('Enter a meal')
    mealname = input()

    mealapi = 'https://www.themealdb.com/api/json/v1/1/search.php?s='+mealname
    mealresponse = requests.request("GET", mealapi)
    first_ingr = mealresponse.text.find("strIngredient1")
    last_ingr = mealresponse.text.find("strMeasure1")
    meal_dict = json.loads("{ "+mealresponse.text[first_ingr-1:last_ingr-2]+" }")
    print(meal_dict)


    
    url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"
    querystring = {"ingr":"apple", "ingr":"banana"}
    #meal_dict keys must all read "ingr" before querystring will accept it as input
    headers = {
	    "X-RapidAPI-Key": "66c11ad3c1mshcab242ab4c9a6abp19ed96jsne88329d755ee",
	    "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
    }


    response = requests.request("GET", url, headers=headers, params=querystring)

    nutrients = response.text.find("nutrients")
    end_nutrients = response.text.find('}')
    nutrient_dict = json.loads(response.text[nutrients+11:end_nutrients+1])

    print(nutrient_dict)


fetch_meal()