import PySimpleGUI as gui

gui.theme('BluePurple')

inputBoxWidth = 10

Left_Wheels_Column = [
    [
        gui.Text('Front Left Front', justification='right', expand_x=True, pad=((5,5),(115,5))), gui.InputText(size=inputBoxWidth, pad=((5,5),(115,5)), enable_events=True)
    ],
    [
        gui.Text('Front Left Rear', justification='right', expand_x=True, pad=((5,5),(1,75))), gui.InputText(size=inputBoxWidth, pad=((5,5),(1,75)), enable_events=True)
    ],
    [
        gui.Text('Rear Left Front', justification='right', expand_x=True), gui.InputText(size=inputBoxWidth, enable_events=True)
    ],
    [
        gui.Text('Rear Left Rear', justification='right', expand_x=True), gui.InputText(size=inputBoxWidth, enable_events=True)
    ],
]

Right_Wheels_Column = [
    [
        gui.InputText(size=inputBoxWidth, pad=((5,5),(115,5)), enable_events=True), gui.Text('Front Right Front', justification='right', expand_x=True, pad=((5,5),(115,5)))
    ],
    [
        gui.InputText(size=inputBoxWidth, pad=((5,5),(1,75)), enable_events=True), gui.Text('Front Right Rear', justification='right', expand_x=True, pad=((5,5),(1,75)))
    ],
    [
        gui.InputText(size=inputBoxWidth, enable_events=True), gui.Text('Rear Right Front', justification='right', expand_x=True)
    ],
    [
         gui.InputText(size=inputBoxWidth, enable_events=True), gui.Text('Rear Right Rear', justification='right', expand_x=True)
    ],
]

Center_Data_Column = [
    [
        gui.Text('Wheel Diameter', justification='center', expand_x=True)
    ],
    [
        gui.InputText(size=inputBoxWidth, pad=(100,0), enable_events=True)
    ],
    [
        gui.Text('****Positive Toe is Tow In****', justification='center', expand_x=True, pad=((5,5),(30,30)))
    ],
    [
        gui.Text('Left Front Toe: ', justification='center', expand_x=True)
    ],
    [
        gui.Text('Right Front Toe: ', justification='center', expand_x=True)
    ],
    [
        gui.Text('Total Front Toe: ', justification='center', expand_x=True, pad=((5,5),(5,50)))
    ],
    [
        gui.Text('Left Rear Toe: ', justification='center', expand_x=True)
    ],
    [
        gui.Text('Right Rear Toe: ', justification='center', expand_x=True)
    ],
    [
        gui.Text('Total Rear Toe: ', justification='center', expand_x=True)
    ]
]

layout=[
    [
        gui.Column(Left_Wheels_Column), gui.Column(Center_Data_Column), gui.Column(Right_Wheels_Column)
    ],
    [
        gui.Button('Clear All'), gui.Push(), gui.Button('Save As')
    ]
]

clearAllConfirmLayout=[
    [
        gui.Text('Are you sure you want to clear all entered values? There will be no way to retrieve this data, afterwards.')
    ],
    [
        gui.Button('No'), gui.Button('Yes')
    ]
]

# Create the Windows
window=gui.Window('String Alignment Assistant', layout)
clearAllWindow=gui.Window('ATTENTION', clearAllConfirmLayout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event == gui.WIN_CLOSED: # if user closes window
        break

    elif event == 'Clear All REMOVE ME TO TEST AGAIN':
        # pop up second window to confirm actions ****THIS DOES NOT WORK****
        try:
            clearAllWindow.un_hide()

        finally:
            while True:
                eventClearAll, valuesClearAll = clearAllWindow.read()

                if eventClearAll in (gui.WIN_CLOSED,'No'):
                    break
                
            clearAllWindow.hide()

    elif event == 'Save As':
        # Ask where to save and stuff
        print('Save As')

    else:
        for x in range(len(values)):
            print('You entered ', values[x], 'in text box', x+1)

window.close()
clearAllWindow.close()