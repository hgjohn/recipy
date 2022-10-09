import requests
import json
import PySimpleGUI as sg



def fetch_meal():
# generates recipe info from selected input
# outputs ingredients, measurements, nutrition, and instructions to display

    
    meal_layout = [  [sg.Text('Input a meal')],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
    
    

    # Create the Window
    window = sg.Window('Meal Search', meal_layout)
# Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Ok':
            meal = values[0]
            print('You entered ', meal)
            window.close()
            

    mealapi = 'https://www.themealdb.com/api/json/v1/1/search.php?s='+meal
    mealresponse = requests.request("GET", mealapi)
    meal_dict = json.loads(mealresponse.text)
    #gets meal names
    meal_iter = 0
    recipe_list = []
    while meal_iter != len(meal_dict['meals']):
        if meal_iter == len(meal_dict['meals']):
            break
        else:
            recipe_list.append(meal_dict['meals'][meal_iter]['strMeal'])
            meal_iter += 1
    #input an available recipe
    
    
    recipe_layout = [  [sg.Text('Input recipe selection')],
            [
        sg.Listbox(
            values = recipe_list, enable_events=True, size=(40, 20), key="-RECIPE LIST-"
        )
    ],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]]

    
    def recipe_select():
        window = sg.Window('Recipe Select', recipe_layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            if event == 'Ok':
                global recipe
                recipe = values[0]
                print('you entered ', recipe)
                window.close()
    
    recipe_select()

    
    
    #gets instructions, ingr, and measurements for recipe
    recipe_iter = 0
    while recipe_iter != len(meal_dict['meals']):
        if recipe_iter == len(meal_dict['meals']):
            break
        elif meal_dict['meals'][recipe_iter]['strMeal'] == recipe:
            recipe_dict = meal_dict['meals'][recipe_iter]
            recipe_iter += 1
        else:
            recipe_iter += 1

    recipe_inst = recipe_dict['strInstructions']
    ingr_list = [recipe_dict['strIngredient1'], recipe_dict['strIngredient2'], recipe_dict['strIngredient3'], recipe_dict['strIngredient4'], recipe_dict['strIngredient5'], recipe_dict['strIngredient6'], recipe_dict['strIngredient7'], recipe_dict['strIngredient8'], recipe_dict['strIngredient9'], recipe_dict['strIngredient10'], recipe_dict['strIngredient11'], recipe_dict['strIngredient12'], recipe_dict['strIngredient13'], recipe_dict['strIngredient14'], recipe_dict['strIngredient15'], recipe_dict['strIngredient16'], recipe_dict['strIngredient17'], recipe_dict['strIngredient18'], recipe_dict['strIngredient19'], recipe_dict['strIngredient20'], ]
    meas_list = [recipe_dict['strMeasure1'], recipe_dict['strMeasure2'], recipe_dict['strMeasure3'], recipe_dict['strMeasure4'], recipe_dict['strMeasure5'], recipe_dict['strMeasure6'], recipe_dict['strMeasure7'], recipe_dict['strMeasure8'], recipe_dict['strMeasure9'], recipe_dict['strMeasure10'], recipe_dict['strMeasure11'], recipe_dict['strMeasure12'], recipe_dict['strMeasure13'], recipe_dict['strMeasure14'], recipe_dict['strMeasure15'], recipe_dict['strMeasure16'], recipe_dict['strMeasure17'], recipe_dict['strMeasure18'], recipe_dict['strMeasure19'], recipe_dict['strMeasure20'], ]
    



    #this empties null values from ingr_list
    ingr_list = list(filter(None, ingr_list))
    ingr_keys = list()


    c = []
    for x, y in zip(ingr_list, meas_list):
        c += [x, y]
    d = str(c)


    #this creates a list with 'ingr' as each value equal in length to the ingr_list
    ingr_info = [ingr_list, ingr_keys]
    max_length = 0
    for array in ingr_info:
        max_length = max(max_length, len(array))

    for array in ingr_info:
        array += ['ingr'] * (max_length - len(array))

    ingr_query = dict(zip(ingr_keys, ingr_list))

    final_layout = [  [sg.Text('Input recipe selection')],
            [sg.Text('Ingredients')],
    [sg.Multiline(d, size=(45, 5), expand_x=False, expand_y=True, key='-INGREDIENTMLINE-')],
    [sg.Text('Directions')],
    [sg.Multiline(recipe_inst, size=(45, 5), expand_x=False, expand_y=True, key='-DIRECTIONMLINE-')]
    ]
    
    def final_boss():
        window = sg.Window('Recipe info', final_layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
        

    final_boss()

    
    #api call for nutrition based on ingr dict
    url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"
    #querystring = {"ingr":"apple", "ingr":"banana"}
    querystring = ingr_query
    #meal_dict keys must all read "ingr" before querystring will accept it as input
    headers = {
	    "X-RapidAPI-Key": "66c11ad3c1mshcab242ab4c9a6abp19ed96jsne88329d755ee",
	    "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    nutrients = response.text.find("nutrients")
    end_nutrients = response.text.find('}')
    nutrient_dict = json.loads(response.text[nutrients+11:end_nutrients+1])

    nutrient_code = {'FIBTG': 'Fiber', 'CHOCDF': 'Carbohydrates', 'ENERC_KCAL': 'Kilocalories', 'FAT': 'Total fat', 'PROCNT': 'Protein'}

    
    
    #print(ingr_query)
    #print(ingr_list)
    #print(meas_list)
    #print(recipe_inst)
    #print(nutrient_dict)

    


fetch_meal()

# put ingr in dict with 'ingr' for each key for nutrition
# convert nutrition symbols to strings