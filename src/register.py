import PySimpleGUI as sg
import csv
from login import load_users

sg.theme('LightGreen3')

BTN_SIZE = (40, 2)
F_SIZE = (40, 2)
YELLOW = "#DEBE97"
TITLE_SIZE = "24px"

LAYOUT_REGISTER = [
    [sg.Text('Registrasi', font=TITLE_SIZE, size=F_SIZE, justification="center")],
    [sg.Text('Username', size=BTN_SIZE), sg.InputText(key='USERNAME_REG',do_not_clear=False)],
    [sg.Text('Password', size=BTN_SIZE), sg.InputText(key='PASSWORD_REG', password_char='*', do_not_clear=False)],
    [sg.Combo(['Pasien', 'Dokter'], key='ROLE', size=BTN_SIZE)],
    [sg.Button('Register', key='AFTER_REGISTER', size=BTN_SIZE)],
    [sg.Button('Back', key='MAIN_BEFORE_LOGIN', button_color=YELLOW, size=BTN_SIZE)]
]

LAYOUT_AFTER_REGISTER = [
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