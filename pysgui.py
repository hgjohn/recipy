import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window
recipe_layout = [  [sg.Text('Input recipe selection')],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]]

meal_layout = [  [sg.Text('Input a meal')],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

def recipe_select():
    window = sg.Window('Recipe Select', recipe_layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Ok':
            recipe = values[0]
            print('you entered ', recipe)
            window.close()


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
        recipe_select()
        


#assign functions to button press

#first window - accept meal input, assign to variable
#second window - display recipes available in list box, accept recipe input, assign to variable
#third window - display instructions, ingredients, amounts, and nutrition of input recipe