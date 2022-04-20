import PySimpleGUI as sg
from login import LAYOUT_LOGIN
from register import LAYOUT_REGISTER
from klinik_terdekat import LAYOUT_KLINIK
from doktercekjadwal import LAYOUT_CEK_JADWAL, get_request
from klinik_terdekat import LAYOUT_KLINIK, klinik

# sg.theme('LightGreen3')

BTN_SIZE = (40, 2)
F_SIZE = (40, 2)
YELLOW = "#DEBE97"
TITLE_SIZE = "24px"

LAYOUT_MAIN_BEFORE_LOGIN = [
    [sg.Text('Main Menu', font=TITLE_SIZE, size=F_SIZE, justification="center")],
    [sg.Button('Login', key='LOGIN', size=BTN_SIZE)],
    [sg.Button('Registrasi', key='REGISTER', size=BTN_SIZE)],
    [sg.Button('Exit', button_color=YELLOW, size=BTN_SIZE)]
]

LAYOUT_MAIN_AFTER_LOGIN_PASIEN = [
    [sg.Text('Main Menu Pasien', font=TITLE_SIZE, size=F_SIZE, justification="center")],
    [sg.Button('Daftar Check Up', key='KLINIK', size=BTN_SIZE)],
    [sg.Text('')],
    [sg.Button('Logout', key='LAYOUT_MAIN_BEFORE_LOGIN'), sg.Button('Exit')]
]

LAYOUT_MAIN_AFTER_LOGIN_DOKTER = [
    [sg.Text('Main Menu Dokter', font=TITLE_SIZE, size=F_SIZE, justification="center")],
    [sg.Button('Cek Jadwal', key='CEK_JADWAL', size=BTN_SIZE)],
    [sg.Text('')],
    [sg.Button('Logout', key='LAYOUT_MAIN_BEFORE_LOGIN'), sg.Button('Exit')]
]

LAYOUT = [
    [
        sg.Column(LAYOUT_MAIN_BEFORE_LOGIN, key='LAYOUT_MAIN_BEFORE_LOGIN', element_justification='c'),
        sg.Column(LAYOUT_LOGIN, visible=False, key='LAYOUT_LOGIN', element_justification='c'),
        sg.Column(LAYOUT_REGISTER, visible=False, key='LAYOUT_REGISTER', element_justification='c'),
        sg.Column(LAYOUT_MAIN_AFTER_LOGIN_DOKTER, visible=False, key='LAYOUT_MAIN_AFTER_LOGIN_DOKTER', element_justification='c'),
        sg.Column(LAYOUT_MAIN_AFTER_LOGIN_PASIEN, visible=False, key='LAYOUT_MAIN_AFTER_LOGIN_PASIEN', element_justification='c'),
        sg.Column(LAYOUT_KLINIK, visible=False, key='LAYOUT_KLINIK'),
        sg.Column(LAYOUT_CEK_JADWAL, visible=False, key='LAYOUT_CEK_JADWAL')
    ]
]

window = sg.Window('Clinicare', LAYOUT)

LAYOUT = 'MAIN_BEFORE_LOGIN'

while True:
    event, values = window.read()
    print(event, values)

    if event in ('LOGIN', 'REGISTER', 'KLINIK'):
        window[f'LAYOUT_{LAYOUT}'].update(visible=False)
        LAYOUT = event
        window[f'LAYOUT_{LAYOUT}'].update(visible=True)

    elif 'MAIN_AFTER_LOGIN_PASIEN' in event:
        window[f'LAYOUT_{LAYOUT}'].update(visible=False)
        LAYOUT = 'MAIN_AFTER_LOGIN_PASIEN'
        window[f'LAYOUT_{LAYOUT}'].update(visible=True)

    elif 'MAIN_AFTER_LOGIN_DOKTER' in event:
        window[f'LAYOUT_{LAYOUT}'].update(visible=False)
        LAYOUT = 'MAIN_AFTER_LOGIN_DOKTER'
        window[f'LAYOUT_{LAYOUT}'].update(visible=True)

    elif 'MAIN_BEFORE_LOGIN' in event:
        window[f'LAYOUT_{LAYOUT}'].update(visible=False)
        LAYOUT = 'MAIN_BEFORE_LOGIN'
        window[f'LAYOUT_{LAYOUT}'].update(visible=True)
    
    elif event in ('CEK_JADWAL'):
        window[f'LAYOUT_{LAYOUT}'].update(visible=False)
        LAYOUT = 'CEK_JADWAL'         
        window[f'LAYOUT_{LAYOUT}'].update(visible=True)
        for i in range(len(get_request())):
            if UNAME != get_request()[i]["dokter"]:
                window['JADWAL'+str(i)].update(visible=True)

    if event == 'Cari':
        for i in range(len(klinik)):
            if values[0].lower() == klinik[i]['provinsi'].lower() and values[1].lower() == klinik[i]['kota'].lower():
                window[str(i)].update(visible=True)
            else:
                window[str(i)].update(visible=False)


    if event == sg.WIN_CLOSED or 'Exit' in event:
        break

window.close()