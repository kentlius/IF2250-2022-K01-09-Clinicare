
import csv
import PySimpleGUI as sg
from style import BTN_SIZE, F_SIZE, YELLOW, TITLE_SIZE

sg.theme('LightGreen3')

LAYOUT_LOGIN = [
    [sg.Text('Login', font=TITLE_SIZE, size=F_SIZE, justification="center")],
    [sg.Button('Login Pasien', key='LOGIN_PASIEN', size=BTN_SIZE)],
    [sg.Button('Login Dokter', key='LOGIN_DOKTER', size=BTN_SIZE)],
    [sg.Button('Back', key='MAIN_BEFORE_LOGIN', button_color=YELLOW, size=BTN_SIZE)]
]

LAYOUT_LOGIN_PASIEN = [
    [sg.Text('Login Pasien', font=TITLE_SIZE, size=F_SIZE, justification="center")],
    [sg.Text('Username', size=BTN_SIZE), sg.InputText(key='USERNAME_P',do_not_clear=True)],
    [sg.Text('Password', size=BTN_SIZE), sg.InputText(key='PASSWORD_P', password_char='*', do_not_clear=True)],
    [sg.Button('Login', key='MAIN_AFTER_LOGIN_PASIEN', button_color=YELLOW, size=BTN_SIZE)],
    [sg.Button('Back', key='MAIN_BEFORE_LOGIN', button_color=YELLOW, size=BTN_SIZE)]
]

LAYOUT_LOGIN_DOKTER = [
    [sg.Text('Login Pasien', font=TITLE_SIZE, size=F_SIZE, justification="center")],
    [sg.Text('Username', size=BTN_SIZE), sg.InputText(key='USERNAME_D',do_not_clear=True)],
    [sg.Text('Password', size=BTN_SIZE), sg.InputText(key='PASSWORD_D', password_char='*', do_not_clear=True)],
    [sg.Button('Login', key='MAIN_AFTER_LOGIN_DOKTER', button_color=YELLOW, size=BTN_SIZE)],
    [sg.Button('Back', key='MAIN_BEFORE_LOGIN', button_color=YELLOW, size=BTN_SIZE)]
]

def load_users(role):
    users = []
    with open('../src/data/'+role+'.txt', encoding="UTF-8") as user_list:
        user = csv.reader(user_list, delimiter=',')
        for each_user in user:
            users.append({'username': each_user[0], 'password': each_user[2]})
    return users

def auth_login(username,password,role):
    users = load_users(role)
    for each_user in users:
        if each_user['username'] == username and each_user['password'] == password:
            return 0
    return 1
