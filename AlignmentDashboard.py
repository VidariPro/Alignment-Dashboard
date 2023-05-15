import PySimpleGUI as gui
import math

gui.theme('BluePurple')

inputBoxWidth = 10
FLToe_Deg = 0
FRToe_Deg = 0
RLToe_Deg = 0
RRToe_Deg = 0

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
        gui.Text(key='LeftFrontToe', justification='center', expand_x=True)
    ],
    [
        gui.Text(key='RightFrontToe', justification='center', expand_x=True)
    ],
    [
        gui.Text('Total Front Toe: ' + ' degrees', justification='center', expand_x=True, pad=((5,5),(5,50)))
    ],
    [
        gui.Text(key='LeftRearToe', justification='center', expand_x=True)
    ],
    [
        gui.Text(key='RightRearToe', justification='center', expand_x=True)
    ],
    [
        gui.Text('Total Rear Toe: ' + ' degrees', justification='center', expand_x=True)
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

def toeCalcs(inputs):
    wheelDia = inputs[4]
    FLF_Measured = inputs[0]
    FLR_Measured = inputs[1]
    RLF_Measured = inputs[2]
    RLR_Measured = inputs[3]
    FRF_Measured = inputs[5]
    FRR_Measured = inputs[6]
    RRF_Measured = inputs[7]
    RRR_Measured = inputs[8]

    FL_Toe = round(math.degrees(math.asin((FLF_Measured-FLR_Measured)/wheelDia)), 2)
    FR_Toe = round(math.degrees(math.asin((FRF_Measured-FRR_Measured)/wheelDia)), 2)
    RL_Toe = round(math.degrees(math.asin((RLF_Measured-RLR_Measured)/wheelDia)), 2)
    RR_Toe = round(math.degrees(math.asin((RRF_Measured-RRR_Measured)/wheelDia)), 2)

    toeAngles = [FL_Toe, FR_Toe, RL_Toe, RR_Toe]
    
    return toeAngles

# Create the Windows
window=gui.Window('String Alignment Assistant', layout, finalize=True)
clearAllWindow=gui.Window('ATTENTION', clearAllConfirmLayout)

window['LeftFrontToe'].update('Left Front Toe: ' + str(FLToe_Deg) + ' degrees')
window['RightFrontToe'].update('Right Front Toe: ' + str(FRToe_Deg) + ' degrees')

window['LeftRearToe'].update('Left Rear Toe: ' + str(RLToe_Deg) + ' degrees')
window['RightRearToe'].update('Right Rear Toe: ' + str(RRToe_Deg) + ' degrees')

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
        #if '' in values:
        #    print('Not all values entered')
        #else:
        for x in range(len(values)):
            if values[x] == '':
                values[x] = 2
            else:
                values[x] = float(values[x])

        results = toeCalcs(values)

        FLToe_Deg = results[0]
        FRToe_Deg = results[1]
        RLToe_Deg = results[2]
        RRToe_Deg = results[3]

        window['LeftFrontToe'].update('Left Front Toe: ' + str(FLToe_Deg) + ' degrees')
        window['RightFrontToe'].update('Right Front Toe: ' + str(FRToe_Deg) + ' degrees')

        window['LeftRearToe'].update('Left Rear Toe: ' + str(RLToe_Deg) + ' degrees')
        window['RightRearToe'].update('Right Rear Toe: ' + str(RRToe_Deg) + ' degrees')

        window.refresh()

window.close()
clearAllWindow.close()