# reciPy.py

import PySimpleGUI as sg

# Changes the theme/color 
# It's a place holder for now, until I figure out the values
# sg.theme('')

# ----- child components
# meal names will be given to values as an array. Key can be referenced in the event loop.

recipe_searcher_column = [
    [sg.InputText(), sg.Button('Search')],
    [
        sg.Listbox(
            values = [], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
    [sg.Button('Back'), sg.Button('Next')],
    [sg.Button("OK")]
]  

#Displays meal information
#We have the option of displaying a picture, if we grab that link
recipe_viewer_column = [
    [sg.Text('Ingredients')],
    [sg.Text('Directions')]
    
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
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()