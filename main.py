import PySimpleGUI as sg


def create_window(theme):
    sg.theme(theme)
    print(sg.theme_list())  # prints all themes

    button_size = (6, 3)
    sg.set_options(font="Franklin 14", button_element_size=button_size)

    layout = [
        [
            sg.Text(
                "output",
                key="-OUTPUT-",
                font="Franklin 26",
                justification="right",
                expand_x=True,
                pad=(10, 20),
            )
        ],
        [
            sg.Button("Clear", key="-CLEAR-", expand_x=True),
            sg.Button("Enter", key="-ENTER-", expand_x=True),
        ],
        [
            sg.Button("7", key="-7-", size=button_size),
            sg.Button("8", key="-8-", size=button_size),
            sg.Button("9", key="-9-", size=button_size),
            sg.Button("*", key="-*-", size=button_size),
        ],
        [
            sg.Button("4", key="-4-", size=button_size),
            sg.Button("5", key="-5-", size=button_size),
            sg.Button("6", key="-6-", size=button_size),
            sg.Button("/", key="-/-", size=button_size),
        ],
        [
            sg.Button("1", key="-1-", size=button_size),
            sg.Button("2", key="-2-", size=button_size),
            sg.Button("3", key="-3-", size=button_size),
            sg.Button("-", key="---", size=button_size),
        ],
        [
            sg.Button("0", key="-0-", expand_x=True),
            sg.Button(".", key="-.-", size=button_size),
            sg.Button("+", key="-+-", size=button_size),
        ],
    ]
    return sg.Window("Title", layout)


window = create_window("dark")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
