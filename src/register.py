import csv
import PySimpleGUI as sg
from login import load_users
from klinik_terdekat import load_klinik
sg.theme('LightGreen3')

BTN_SIZE = (40, 2)
F_SIZE = (40, 2)
YELLOW = "#DEBE97"
TITLE_SIZE = "24px"

Pasien_layout =   [[sg.Text('PASIEN', background_color='darkseagreen', justification="center")],
                [sg.Text('Username', size=BTN_SIZE, background_color='darkseagreen'), sg.InputText(key='USERNAME_REG_P',do_not_clear=False)],
                [sg.Text('Password', size=BTN_SIZE, background_color='darkseagreen'), sg.InputText(key='PASSWORD_REG_P', password_char='*', do_not_clear=False)],
                [sg.Text('Nama Lengkap', size=BTN_SIZE,background_color='darkseagreen'), sg.InputText(key='NAME_REG_P', do_not_clear=False)],
                [sg.Text('Alamat', size=BTN_SIZE,background_color='darkseagreen'), sg.InputText(key='ALAMAT_REG_P', do_not_clear=False)],
                [sg.Button('Register', key='AFTER_REGISTER_P', size=BTN_SIZE)]]


Dokter_layout =   [[sg.Text('DOKTER',justification="center")],
                [sg.Text('Username', size=BTN_SIZE), sg.InputText(key='USERNAME_REG_D',do_not_clear=False)],
                [sg.Text('Password', size=BTN_SIZE), sg.InputText(key='PASSWORD_REG_D', password_char='*', do_not_clear=False)],
                [sg.Text('Nama Lengkap', size=BTN_SIZE), sg.InputText(key='NAME_REG_D', do_not_clear=False)],
                [sg.Text('Nama Klinik', size=BTN_SIZE), sg.InputText(key='KLINIK_REG_D', do_not_clear=False)],
                [sg.Text('Alamat Klinik', size=BTN_SIZE), sg.InputText(key='ALAMAT_REG_D', do_not_clear=False)],
                [sg.Text('Provinsi', size=(10,2)), sg.InputText(key='PROVINSI_REG_D', do_not_clear=False, size=(30,2)),sg.Text('Kota', size=(10,2)), sg.InputText(key='KOTA_REG_D', do_not_clear=False, size=(30,2))],
                [sg.Text('Jam Buka', size=(10,2)), sg.InputText(key='JAM_BUKA', do_not_clear=False, size=(30,2)),sg.Text('Jam Tutup', size=(10,2)), sg.InputText(key='JAM_TUTUP', do_not_clear=False, size=(30,2))],
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
def auth_register(username,role):
    users = load_users(role)
    for each_user in users:
        if each_user['username'] == username:
            return False
    return True

def doc_register(username, nama, password, klinik):
    with open('./src/data/Doktor.txt', 'a', encoding="UTF-8") as doc_list:
        docs = csv.writer(doc_list, delimiter=',', lineterminator='\n')
        docs.writerow([username, nama, password, klinik])

def klinik_register(nama,alamat,kabkota,provinsi,jambuka,jamtutup):
    kliniks = load_klinik()
    exist = False
    for each_klinik in kliniks:
        if each_klinik['nama_klinik'] == nama:
            exist = True
    if not exist:
        with open('./src/data/klinik.txt', encoding="UTF-8") as klinik_list:
            klinik = csv.reader(klinik_list, delimiter=',')
            klinik.writerow([nama,alamat,kabkota,provinsi,jambuka,jamtutup])

def pas_register(username,name,password,address):
    with open('./src/data/Pasien.txt', 'a', encoding="UTF-8") as pas_list:
        pas = csv.writer(pas_list, delimiter=',', lineterminator='\n')
        pas.writerow([username,name,password,address])
