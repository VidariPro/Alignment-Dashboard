import PySimpleGUI as gui
import math

gui.theme('BluePurple')

# Define global variables
inputBoxWidth = 10

FLToe_Deg = 0
FRToe_Deg = 0
TotFToe_Deg = 0

RLToe_Deg = 0
RRToe_Deg = 0
TotRToe_Deg = 0

# Define variables to be used in layout variable used during main window creation to format window.
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
        gui.InputText(size=inputBoxWidth, pad=(100,0), enable_events=True, focus=True)
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
        gui.Text(key='TotalFrontToe', justification='center', expand_x=True, pad=((5,5),(5,50)))
    ],
    [
        gui.Text(key='LeftRearToe', justification='center', expand_x=True)
    ],
    [
        gui.Text(key='RightRearToe', justification='center', expand_x=True)
    ],
    [
        gui.Text(key='TotalRearToe', justification='center', expand_x=True)
    ]
]

# Define layout variable to be used in main window creation to format window
layout=[
    [
        gui.Column(Left_Wheels_Column), gui.Column(Center_Data_Column), gui.Column(Right_Wheels_Column)
    ],
    [
        gui.Button('Clear All'), gui.Push(), gui.Button('Save As')
    ]
]

# Define layout varable to be used in warning box window creation for format window
clearAllConfirmLayout=[
    [
        gui.Text('Are you sure you want to clear all entered values? There will be no way to retrieve this data, afterwards.')
    ],
    [
        gui.Button('No'), gui.Button('Yes')
    ]
]

# Function to calculate front toe angle from measurements input into console. Returns list of angles.
def frontToeCalcs(inputs):
    wheelDia = inputs[4]
    FLF_Measured = inputs[0]
    FLR_Measured = inputs[1]
    FRF_Measured = inputs[5]
    FRR_Measured = inputs[6]

    try:
        FL_Toe = round(math.degrees(math.asin((FLF_Measured-FLR_Measured)/wheelDia)), 2)
        FR_Toe = round(math.degrees(math.asin((FRF_Measured-FRR_Measured)/wheelDia)), 2)
    except:
        FL_Toe = 0
        FR_Toe = 0
    
    frontToeAngles = [FL_Toe, FR_Toe]
    
    return frontToeAngles

# Function to calculate rear toe angle from measurements input into console. Returns list of angles.
def rearToeCalcs(inputs):
    wheelDia = inputs[4]
    RLF_Measured = inputs[2]
    RLR_Measured = inputs[3]
    RRF_Measured = inputs[7]
    RRR_Measured = inputs[8]

    try:
        RL_Toe = round(math.degrees(math.asin((RLF_Measured-RLR_Measured)/wheelDia)), 2)
        RR_Toe = round(math.degrees(math.asin((RRF_Measured-RRR_Measured)/wheelDia)), 2)
    except:
        RL_Toe = 0
        RR_Toe = 0

    rearToeAngles = [RL_Toe, RR_Toe]
    
    return rearToeAngles

# Create the windows
window=gui.Window('String Alignment Assistant', layout, finalize=True)
clearAllWindow=gui.Window('ATTENTION', clearAllConfirmLayout)

# Create calculated toe angle strings
window['LeftFrontToe'].update('Left Front Toe: ' + str(FLToe_Deg) + ' degrees')
window['RightFrontToe'].update('Right Front Toe: ' + str(FRToe_Deg) + ' degrees')
window['TotalFrontToe'].update('Total Front Toe: ' + str(TotFToe_Deg) + ' degrees')

window['LeftRearToe'].update('Left Rear Toe: ' + str(RLToe_Deg) + ' degrees')
window['RightRearToe'].update('Right Rear Toe: ' + str(RRToe_Deg) + ' degrees')
window['TotalRearToe'].update('Total Rear Toe: ' + str(TotRToe_Deg) + ' degrees')

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
        if '' not in (values[0], values[1], values[5], values[6], values[4]):
            for x in range(len(values)):
                if values[x] != '':
                    try:
                        values[x] = float(values[x])
                    except:
                        continue

            frontResults = frontToeCalcs(values)

            # Update front *_Deg variables with calculated values
            FLToe_Deg = frontResults[0]
            FRToe_Deg = frontResults[1]
            TotFToe_Deg = round(frontResults[0] + frontResults[1], 2)

            # Updates front calculated toe angle strings with newly calculated values
            window['LeftFrontToe'].update('Left Front Toe: ' + str(FLToe_Deg) + ' degrees')
            window['RightFrontToe'].update('Right Front Toe: ' + str(FRToe_Deg) + ' degrees')
            window['TotalFrontToe'].update('Total Front Toe: ' + str(TotFToe_Deg) + ' degrees')
        else:
            # Update front *_Deg variables with 0's
            FLToe_Deg = 0
            FRToe_Deg = 0
            TotFToe_Deg = 0

            # Updates front calculated toe angle strings with 0 strings
            window['LeftFrontToe'].update('Left Front Toe: ' + str(FLToe_Deg) + ' degrees')
            window['RightFrontToe'].update('Right Front Toe: ' + str(FRToe_Deg) + ' degrees')
            window['TotalFrontToe'].update('Total Front Toe: ' + str(TotFToe_Deg) + ' degrees')

        if '' not in (values[2], values[3], values[7], values[8], values[4]):
            for x in range(len(values)):
                if values[x] != '':
                    try:
                        values[x] = float(values[x])
                    except:
                        continue
            
            rearResults = rearToeCalcs(values)

            # Update rear *_Deg variables with calculated values
            RLToe_Deg = rearResults[0]
            RRToe_Deg = rearResults[1]
            TotRToe_Deg = round(rearResults[0] + rearResults[1], 2)

            # Updates rear calculated toe angle strings with newly calculated values
            window['LeftRearToe'].update('Left Rear Toe: ' + str(RLToe_Deg) + ' degrees')
            window['RightRearToe'].update('Right Rear Toe: ' + str(RRToe_Deg) + ' degrees')
            window['TotalRearToe'].update('Total Rear Toe: ' + str(TotRToe_Deg) + ' degrees')
        else:
            # Update rear *_Deg variables with 0's
            RLToe_Deg = 0
            RRToe_Deg = 0
            TotRToe_Deg = 0

            # Updates rear calculated toe angle strings with 0 strings
            window['LeftRearToe'].update('Left Rear Toe: ' + str(RLToe_Deg) + ' degrees')
            window['RightRearToe'].update('Right Rear Toe: ' + str(RRToe_Deg) + ' degrees')
            window['TotalRearToe'].update('Total Rear Toe: ' + str(TotRToe_Deg) + ' degrees')

        # Refresh main window to display updated elements
        window.refresh()

# Clean up windows at program end
window.close()
clearAllWindow.close()