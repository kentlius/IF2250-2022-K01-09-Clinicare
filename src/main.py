import PySimpleGUI as sg

from login import LAYOUT_LOGIN, LAYOUT_LOGIN_PASIEN, LAYOUT_LOGIN_DOKTER, auth_login
from register import LAYOUT_REGISTER, LAYOUT_AFTER_REGISTER_P, LAYOUT_AFTER_REGISTER_D, auth_register, doc_register, pas_register
from klinik_terdekat import LAYOUT_KLINIK, data_klinik

sg.theme('LightGreen3')

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
    [sg.Button('Cek Request', size=BTN_SIZE)],
    [sg.Text('')],
    [sg.Button('Logout', key='LAYOUT_MAIN_BEFORE_LOGIN'), sg.Button('Exit')]
]

LAYOUT = [
    [
        sg.Column(LAYOUT_MAIN_BEFORE_LOGIN, key='LAYOUT_MAIN_BEFORE_LOGIN', element_justification='c'),
        sg.Column(LAYOUT_LOGIN, visible=False, key='LAYOUT_LOGIN', element_justification='c'),
        sg.Column(LAYOUT_LOGIN_PASIEN, visible=False, key='LAYOUT_LOGIN_PASIEN', element_justification='c'),
        sg.Column(LAYOUT_LOGIN_DOKTER, visible=False, key='LAYOUT_LOGIN_DOKTER', element_justification='c'),
        sg.Column(LAYOUT_REGISTER, visible=False, key='LAYOUT_REGISTER', element_justification='c'),
        sg.Column(LAYOUT_AFTER_REGISTER_P, visible=False, key='LAYOUT_AFTER_REGISTER_P', element_justification='c'),
        sg.Column(LAYOUT_AFTER_REGISTER_D, visible=False, key='LAYOUT_AFTER_REGISTER_D', element_justification='c'),
        sg.Column(LAYOUT_MAIN_AFTER_LOGIN_DOKTER, visible=False, key='LAYOUT_MAIN_AFTER_LOGIN_DOKTER', element_justification='c'),
        sg.Column(LAYOUT_MAIN_AFTER_LOGIN_PASIEN, visible=False, key='LAYOUT_MAIN_AFTER_LOGIN_PASIEN', element_justification='c'),
        sg.Column(LAYOUT_KLINIK, visible=False, key='LAYOUT_KLINIK')
    ]
]

window = sg.Window('Clinicare', LAYOUT)

LAYOUT = 'MAIN_BEFORE_LOGIN'

ROLE = ""
while True:
    event, values = window.read()
    print(event, values, ROLE)
    if event in ('LOGIN', 'REGISTER', 'KLINIK'):
        window[f'LAYOUT_{LAYOUT}'].update(visible=False)
        LAYOUT = event
        window[f'LAYOUT_{LAYOUT}'].update(visible=True)

    elif event in ('LOGIN_PASIEN'):
        window[f'LAYOUT_{LAYOUT}'].update(visible=False)
        LAYOUT = event
        ROLE = 'Pasien'
        window[f'LAYOUT_{LAYOUT}'].update(visible=True)

    elif event in ('LOGIN_DOKTER'):
        window[f'LAYOUT_{LAYOUT}'].update(visible=False)
        LAYOUT = event
        ROLE = 'Dokter'
        window[f'LAYOUT_{LAYOUT}'].update(visible=True)

    elif 'MAIN_AFTER_LOGIN' in event:
        window[f'LAYOUT_{LAYOUT}'].update(visible=False)
        if ROLE=='Pasien':
            UNAME = str(values['USERNAME_P'])
            PW = str(values['PASSWORD_P'])
        else :
            UNAME = str(values['USERNAME_D'])
            PW = str(values['PASSWORD_D'])
        if not UNAME:
            sg.Popup('Username tidak boleh kosong')
        elif not PW:
            sg.Popup('Password tidak boleh kosong')
        elif auth_login(UNAME, PW, ROLE)==1:
            sg.Popup('Username atau Password salah')
        elif auth_login(UNAME, PW, ROLE)==0:
            sg.Popup('Jenis akun salah')
        else:
            LAYOUT = event
        window[f'LAYOUT_{LAYOUT}'].update(visible=True)

    elif 'AFTER_REGISTER_P' in event:
        window[f'LAYOUT_{LAYOUT}'].update(visible=False)
        UNAME = str(values['USERNAME_REG_P'])
        PW = str(values['PASSWORD_REG_P'])
        if not UNAME:
            sg.Popup('Username tidak boleh kosong')
        elif not PW:
            sg.Popup('Password tidak boleh kosong')
        elif auth_register(UNAME, PW, 'Pasien')==0:
            sg.Popup('Username sudah dipakai')
        else:
            pas_register(str(values["NAME_REG_P"]),str(values["ALAMAT_REG_P"]))
            LAYOUT = event
        window[f'LAYOUT_{LAYOUT}'].update(visible=True)

    elif 'AFTER_REGISTER_D' in event:
        window[f'LAYOUT_{LAYOUT}'].update(visible=False)
        UNAME = str(values['USERNAME_REG_D'])
        PW = str(values['PASSWORD_REG_D'])
        if not UNAME:
            sg.Popup('Username tidak boleh kosong')
        elif not PW:
            sg.Popup('Password tidak boleh kosong')
        elif auth_register(UNAME, PW, 'Dokter')==0:
            sg.Popup('Username sudah dipakai')
        else:
            doc_register(str(values['NAME_REG_D']), str(values['KLINIK_REG_D']), str(values['ALAMAT_REG_D']), str(values['PROVINSI_REG_D']), str(values['KOTA_REG_D']), str(values['JAM_BUKA']), str(values['JAM_TUTUP']))
            LAYOUT = event
        window[f'LAYOUT_{LAYOUT}'].update(visible=True)

    elif 'MAIN_BEFORE_LOGIN' in event:
        window[f'LAYOUT_{LAYOUT}'].update(visible=False)
        LAYOUT = 'MAIN_BEFORE_LOGIN'
        window[f'LAYOUT_{LAYOUT}'].update(visible=True)

    if event == 'Cari':
        for i in range(len(data_klinik)):
            if values[0].lower() == data_klinik[i]['provinsi'].lower() and values[1].lower() == data_klinik[i]['kota'].lower():
                window[str(i)].update(visible=True)
            else:
                window[str(i)].update(visible=False)

    if event == sg.WIN_CLOSED or 'Exit' in event:
        break

window.close()
