import PySimpleGUI as sg

sg.theme('LightGreen3')

BTN_SIZE = (40, 2)
F_SIZE = (40, 2)
YELLOW = "#DEBE97"
TITLE_SIZE = "24px"

LAYOUT_LOGIN = [
    [sg.Text('Login', font=TITLE_SIZE, size=F_SIZE, justification="center")],
    [sg.Button('Login Pasien', key='MAIN_AFTER_LOGIN_PASIEN', size=BTN_SIZE)],
    [sg.Button('Login Dokter', key='MAIN_AFTER_LOGIN_DOKTER', size=BTN_SIZE)],
    [sg.Button('Back', key='MAIN_BEFORE_LOGIN', button_color=YELLOW, size=BTN_SIZE)]
]
