# reciPy.py

import PySimpleGUI as sg
import requests
import json

def list_meal(mealname):
# generates recipe info from selected input
# outputs ingredients, measurements, nutrition, and instructions to display

    mealapi = 'https://www.themealdb.com/api/json/v1/1/search.php?s='+mealname
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
    return recipe_list

#list_meal('chicken')

def get_mealingr(mealname):

    mealapi = 'https://www.themealdb.com/api/json/v1/1/search.php?s='+mealname
    mealresponse = requests.request("GET", mealapi)
    meal_dict = json.loads(mealresponse.text)
    #input an available recipe
    
    #gets instructions, ingr, and measurements for recipe
    recipe_iter = 0
    while recipe_iter != len(meal_dict['meals']):
        if recipe_iter == len(meal_dict['meals']):
            break
        elif meal_dict['meals'][recipe_iter]['strMeal'] == mealname:
            recipe_dict = meal_dict['meals'][recipe_iter]
            recipe_iter += 1
        else:
            recipe_iter += 1

    recipe_inst = recipe_dict['strInstructions']
    ingr_list = [recipe_dict['strIngredient1'], recipe_dict['strIngredient2'], recipe_dict['strIngredient3'], recipe_dict['strIngredient4'], recipe_dict['strIngredient5'], recipe_dict['strIngredient6'], recipe_dict['strIngredient7'], recipe_dict['strIngredient8'], recipe_dict['strIngredient9'], recipe_dict['strIngredient10'], recipe_dict['strIngredient11'], recipe_dict['strIngredient12'], recipe_dict['strIngredient13'], recipe_dict['strIngredient14'], recipe_dict['strIngredient15'], recipe_dict['strIngredient16'], recipe_dict['strIngredient17'], recipe_dict['strIngredient18'], recipe_dict['strIngredient19'], recipe_dict['strIngredient20'], ]
    meas_list = [recipe_dict['strMeasure1'], recipe_dict['strMeasure2'], recipe_dict['strMeasure3'], recipe_dict['strMeasure4'], recipe_dict['strMeasure5'], recipe_dict['strMeasure6'], recipe_dict['strMeasure7'], recipe_dict['strMeasure8'], recipe_dict['strMeasure9'], recipe_dict['strMeasure10'], recipe_dict['strMeasure11'], recipe_dict['strMeasure12'], recipe_dict['strMeasure13'], recipe_dict['strMeasure14'], recipe_dict['strMeasure15'], recipe_dict['strMeasure16'], recipe_dict['strMeasure17'], recipe_dict['strMeasure18'], recipe_dict['strMeasure19'], recipe_dict['strMeasure20'], ]
    
    #this empties null values from ingr_list
    ingr_list = list(filter(None, ingr_list)) 
    return ingr_list
    #print(ingr_list)   

def get_mealdir(mealname):

    mealapi = 'https://www.themealdb.com/api/json/v1/1/search.php?s='+mealname
    mealresponse = requests.request("GET", mealapi)
    meal_dict = json.loads(mealresponse.text)
    #input an available recipe
    
    #gets instructions, ingr, and measurements for recipe
    recipe_iter = 0
    while recipe_iter != len(meal_dict['meals']):
        if recipe_iter == len(meal_dict['meals']):
            break
        elif meal_dict['meals'][recipe_iter]['strMeal'] == mealname:
            recipe_dict = meal_dict['meals'][recipe_iter]
            recipe_iter += 1
        else:
            recipe_iter += 1
    recipe_inst = recipe_dict['strInstructions']
    return recipe_inst


#get_mealingr('Chicken Handi')


# Changes the theme/color 
# It's a place holder for now, until I figure out the values
# sg.theme('')

# ----- child components
# meal names will be given to values as an array. Key can be referenced in the event loop.

recipe_searcher_column = [
    [
        sg.InputText(size=(45), enable_events=True, key="-MEAL NAME-"), 
        sg.Button('Search')
    ],
    [
        sg.Listbox(
            values = [], enable_events=True, size=(30, 20), key="-RECIPE LIST-"
        )
    ],
    [sg.Button('Back'), sg.Button('Next')],
    [sg.Button("OK")]
]  

#Displays meal information
#We have the option of displaying a picture, if we grab that link
recipe_viewer_column = [
    [sg.Text('Ingredients')],
    [
        sg.Listbox(
            values = [], enable_events=True, size=(45, 5), key="-INGREDIENT LIST-"
        )
    ],
    [sg.Text('Directions')],
    [sg.Multiline('Placeholder', size=(45, 5), expand_x=False, expand_y=True, key='-DIRECTIONMLINE-')]
    
]  

# ----- parent component -----
layout = [
    [
        sg.Column(recipe_searcher_column),
        sg.VSeparator(),
        sg.Column(recipe_viewer_column)
    ]
]  
                     

# Create the window
window = sg.Window("Recipe Browser", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    # This is the part of the code that needs to access Recipe names
    # For example, .update(mealName())
    if event == "Search":
        mealName = values["-MEAL NAME-"]
        window["-RECIPE LIST-"].update(list_meal(mealName))
    if event == "-RECIPE LIST-": # A file was chosen  from the listbox
        recipename = ''.join(values["-RECIPE LIST-"])
        window["-INGREDIENT LIST-"].update(get_mealingr(recipename))
        window["-DIRECTIONMLINE-"].update(get_mealdir(recipename))


window.close()