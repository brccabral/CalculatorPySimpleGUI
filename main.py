import PySimpleGUI as sg


sg.theme("LightGrey1")
print(sg.theme_list())  # prints all themes

sg.set_options(font="Franklin 14")

layout = [
    [sg.Text("output", key="-OUTPUT-")],
    [sg.Button("Clear", key="-CLEAR-"), sg.Button("Enter", key="-ENTER-")],
    [
        sg.Button("7", key="-7-"),
        sg.Button("8", key="-8-"),
        sg.Button("9", key="-9-"),
        sg.Button("*", key="-*-"),
    ],
    [
        sg.Button("4", key="-4-"),
        sg.Button("5", key="-5-"),
        sg.Button("6", key="-6-"),
        sg.Button("/", key="-/-"),
    ],
    [
        sg.Button("1", key="-1-"),
        sg.Button("2", key="-2-"),
        sg.Button("3", key="-3-"),
        sg.Button("-", key="---"),
    ],
    [sg.Button("0", key="-0-"), sg.Button(".", key="-.-"), sg.Button("+", key="-+-")],
]

window = sg.Window("Title", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
