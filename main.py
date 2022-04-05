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
                right_click_menu=theme_menu,
            )
        ],
        [
            sg.Button("Clear", expand_x=True),
            sg.Button("Enter", expand_x=True),
        ],
        [
            sg.Button("7", size=button_size),
            sg.Button("8", size=button_size),
            sg.Button("9", size=button_size),
            sg.Button("*", size=button_size),
        ],
        [
            sg.Button("4", size=button_size),
            sg.Button("5", size=button_size),
            sg.Button("6", size=button_size),
            sg.Button("/", size=button_size),
        ],
        [
            sg.Button("1", size=button_size),
            sg.Button("2", size=button_size),
            sg.Button("3", size=button_size),
            sg.Button("-", size=button_size),
        ],
        [
            sg.Button("0", expand_x=True),
            sg.Button(".", size=button_size),
            sg.Button("+", size=button_size),
        ],
    ]
    return sg.Window("Title", layout)


theme_menu = ["menu", ["LightGrey1", "dark", "DarkGray8", "random"]]
window = create_window("dark")

digits = [f"{number}" for number in range(10)] + ["."]
operations = ["+", "-", "/", "*"]

current_num = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in digits:
        current_num.append(event)
        num_string = "".join(current_num)
        window["-OUTPUT-"].update(num_string)

    if event in operations:
        output: sg.Text = window["-OUTPUT-"]
        full_operation.append(output.DisplayText)
        current_num = []
        full_operation.append(event)
        window["-OUTPUT-"].update("")

    if event in "Enter":
        output: sg.Text = window["-OUTPUT-"]
        full_operation.append(output.DisplayText)
        result = eval(" ".join(full_operation))
        window["-OUTPUT-"].update(result)
        current_num = []
        full_operation = []

    if event in "Clear":
        current_num = []
        full_operation = []
        window["-OUTPUT-"].update("")


window.close()
