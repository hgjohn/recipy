# reciPy.py

import PySimpleGUI as sg

# Changes the theme/color 
# It's a place holder for now, until I figure out the values
# sg.theme('')

# ----- child components
# meal names will be given to values as an array. Key can be referenced in the event loop.

recipe_searcher_column = [
    [
        sg.InputText(enable_events=True, key="-LIST-"), 
        sg.Button('Search')
    ],
    [
        sg.Listbox(
            values = [], enable_events=True, size=(40, 20), key="-INGREDIENT LIST-"
        )
    ],
    [sg.Button('Back'), sg.Button('Next')],
    [sg.Button("OK")]
]  

#Displays meal information
#We have the option of displaying a picture, if we grab that link
recipe_viewer_column = [
    [sg.Text('Ingredients')],
    [sg.Multiline('Placeholder', size=(45, 5), expand_x=False, expand_y=True, key='-INGREDIENTMLINE-')],
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
    #if event == "-LISTRECIPE-":
    #    window["-INGREDIENT LIST-"].update()

window.close()