import PySimpleGUI as gui

gui.theme('BluePurple')

Left_Wheels_Column = [
    [
        gui.Text('Front Left Front'), gui.InputText()
    ],
    [
        gui.Text('Front Left Rear'), gui.InputText()
    ],
    [
        gui.Text('')
    ],
    [
        gui.Text('')
    ],
    [
        gui.Text('Rear Left Front'), gui.InputText()
    ],
    [
        gui.Text('Rear Left Rear'), gui.InputText()
    ],
]

Right_Wheels_Column = [
    [
        gui.Text('Front Right Front'), gui.InputText()
    ],
    [
        gui.Text('Front Right Rear'), gui.InputText()
    ],
    [
        gui.Text('')
    ],
    [
        gui.Text('')
    ],
    [
        gui.Text('Rear Right Front'), gui.InputText()
    ],
    [
        gui.Text('Rear Right Rear'), gui.InputText()
    ],
]

Center_Data_Column = [
    [
        gui.Text('Wheel Diameter'), gui.InputText()
    ],
    [
        gui.Text('****Positive Toe is Tow In****')
    ],
    [
        gui.Text('')
    ],
    [
        gui.Text('')
    ],
    [
        gui.Text('Left Front Toe: ')
    ],
    [
        gui.Text('Right Front Toe: ')
    ],
    [
        gui.Text('Total Front Toe: ')
    ],
    [
        gui.Text('')
    ],
    [
        gui.Text('')
    ],
    [
        gui.Text('Left Rear Toe: ')
    ],
    [
        gui.Text('Right Rear Toe: ')
    ],
    [
        gui.Text('Total Rear Toe: ')
    ]
]

layout = [
    [
        gui.Column(Left_Wheels_Column),
        gui.Column(Center_Data_Column),
        gui.Column(Right_Wheels_Column)
    ]
]

defaultlayout = [  [gui.Text('Test')],
            [gui.Text('Another Test. Give me somthing to say back'), gui.InputText()],
            [gui.Button('Ok'), gui.Button('Cancel')] ]

# Create the Window
window = gui.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0], '. Why are you such a smart ass?')

window.close()