import PySimpleGUI as sg
import requests
import json

def fetch(mealname):
    if(not mealname):
        return None

    api = 'https://www.themealdb.com/api/json/v1/1/search.php?s='+mealname
    response = requests.request("GET", api)
    meal_dict = json.loads(response.text)  
    return meal_dict['meals']

def list_meal(func):

    if(not func):
        return None
    result = []
    for i in func:
        result.append(i['strMeal'])
    return result

def ingredients(func):
    result = []
    counter = 1
    for i in func[0]:
        if(i == 'strIngredient' + str(counter) and func[0][i]): 
            result.append(func[0][i] + ": " + func[0]['strMeasure' + str(counter)])
            counter += 1
    return result



# ----- child -----
recipe_searcher_column = [
    [
        sg.InputText(size=(25), enable_events=True, key="-MEAL NAME-"), 
        sg.Button('Search')
    ],
    [
        sg.Listbox(
            values = [], enable_events=True, size=(30, 20), key="-RECIPE LIST-"
        )
    ],
    [sg.Button("Exit")]
]  

# Displays meal information
recipe_viewer_column = [
    [sg.Text('Ingredients')],
    [
        sg.Listbox(
            values = [], enable_events=True, size=(45, 5), key="-INGREDIENT LIST-"
        )
    ],
    [sg.Text('Directions')],
    [sg.Multiline('', size=(45, 15), expand_x=False, expand_y=True, key='-DIRECTIONMLINE-')]
    
]  

# ----- parent -----
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
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # This is the part of the code that needs to access Recipe names
    # For example, .update(mealName())
    if event == "Search":
        mealname = values["-MEAL NAME-"]
        recipelist = list_meal(fetch(mealname))
        if(not mealname or not recipelist): # A blank, type != string, or otherwise bad input was given
            sg.popup("No results", keep_on_top=False)
        else:
            window["-RECIPE LIST-"].update(recipelist)
    if event == "-RECIPE LIST-" and values["-RECIPE LIST-"]: # A recipe was chosen from the listbox
        recipename = ''.join(values["-RECIPE LIST-"])
        window["-INGREDIENT LIST-"].update(ingredients(fetch(recipename)))
        window["-DIRECTIONMLINE-"].update(fetch(recipename)[0]['strInstructions'])


window.close()

