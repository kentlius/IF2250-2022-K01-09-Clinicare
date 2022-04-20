import PySimpleGUI as sg
import csv
from login import load_users

sg.theme('LightGreen3')

BTN_SIZE = (40, 2)
F_SIZE = (40, 2)
YELLOW = "#DEBE97"
TITLE_SIZE = "24px"

Pasien_layout =   [[sg.Text('PASIEN', background_color='darkseagreen', justification="center")],
                [sg.Text('Username', size=BTN_SIZE, background_color='darkseagreen'), sg.InputText(key='USERNAME_REG_P',do_not_clear=False)],
                [sg.Text('Password', size=BTN_SIZE, background_color='darkseagreen'), sg.InputText(key='PASSWORD_REG_P', password_char='*', do_not_clear=False)],
                [sg.Button('Register', key='AFTER_REGISTER_P', size=BTN_SIZE)]]

Dokter_layout =   [[sg.Text('DOKTER',justification="center")],
                [sg.Text('Username', size=BTN_SIZE), sg.InputText(key='USERNAME_REG_D',do_not_clear=False)],
                [sg.Text('Password', size=BTN_SIZE), sg.InputText(key='PASSWORD_REG_D', password_char='*', do_not_clear=False)],
                [sg.Button('Register', key='AFTER_REGISTER_D', size=BTN_SIZE)]]

LAYOUT_REGISTER = [
    [sg.Text('Registrasi', font=TITLE_SIZE, size=F_SIZE, justification="center")],
    [sg.TabGroup([[sg.Tab('Pasien', Pasien_layout, background_color='darkseagreen', key='ROLE',element_justification='c'),
                         sg.Tab('Dokter', Dokter_layout, key='ROLE',element_justification='c')]], key='-group1-', tab_location='top', selected_title_color='purple')],
    [sg.Button('Back', key='MAIN_BEFORE_LOGIN', button_color=YELLOW, size=BTN_SIZE)]
    ]

LAYOUT_AFTER_REGISTER_P = [
    [sg.Text('ACCOUNT REGISTERED', font=TITLE_SIZE, size=F_SIZE, justification="center")],
    [sg.Button('Back', key='MAIN_BEFORE_LOGIN', button_color=YELLOW, size=BTN_SIZE)]
]

LAYOUT_AFTER_REGISTER_D = [
    [sg.Text('ACCOUNT REGISTERED', font=TITLE_SIZE, size=F_SIZE, justification="center")],
    [sg.Button('Back', key='MAIN_BEFORE_LOGIN', button_color=YELLOW, size=BTN_SIZE)]
]
def auth_register(username,password,role):
    users = load_users()
    for each_user in users:
        if each_user['username'] == username:
            return 0
    with open('./test/users.txt', 'a') as user_list:
        user = csv.writer(user_list, delimiter=',', lineterminator='\n')
        user.writerow([username, password, role])
    return 1