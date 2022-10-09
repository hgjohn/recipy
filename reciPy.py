# reciPy.py

import PySimpleGUI as sg

# Changes the theme/color 
# It's a place holder for now, until I figure out the values
# sg.theme('')

# ----- child components
recipe_searcher_column = [
    [sg.InputText(), sg.Button('Search')],
    [sg.Button('Back'), sg.Button('Next')],
    [sg.Button("OK")]
]  

recipe_browser_column = [
    [sg.Text('Ingredients')],
    
]  

# ----- parent component -----
layout = [
    [
        sg.Column(recipe_searcher_column),
        sg.VSeparator(),
        sg.Column(recipe_browser_column)
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