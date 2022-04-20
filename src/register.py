import PySimpleGUI as sg

sg.theme('LightGreen3')

BTN_SIZE = (40, 2)
F_SIZE = (40, 2)
YELLOW = "#DEBE97"
TITLE_SIZE = "24px"

LAYOUT_REGISTER = [
    [sg.Text('Registrasi', font=TITLE_SIZE, size=F_SIZE, justification="center")],
    [sg.Button('Register', key='MAIN_BEFORE_LOGIN', size=BTN_SIZE)],
    [sg.Button('Back', key='MAIN_BEFORE_LOGIN', button_color=YELLOW, size=BTN_SIZE)]
]
