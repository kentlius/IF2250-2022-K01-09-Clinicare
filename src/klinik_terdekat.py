import PySimpleGUI as sg
import csv

sg.theme('LightGreen3')

BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT = ((10,20), (10, 20))

BANNER = [[sg.Text('Clinicare', font='Any 20', background_color=DARK_HEADER_COLOR)]]

SEARCH_BAR  = [
    [
        sg.Text('Klinik Terdekat', font='Any 20', pad=((10,0), (0, 0))),
        sg.Input('Provinsi', pad=((20, 0),(0, 0)), size=(20,1)),
        sg.Input('Kota', pad=((20, 0),(0, 0)), size=(20,1)),
        sg.Button('Cari', pad=((20, 0),(0, 0)), size=(10,1))
    ]
]

LAYOUT_KLINIK = [
    [sg.Column(BANNER, size=(960, 40), pad=(0,0), background_color=DARK_HEADER_COLOR)],
    [sg.Column(SEARCH_BAR, size=(920, 50), pad=BPAD_TOP)],
]

def load_klinik():
    kliniks = []
    with open('./test/klinik.txt') as klinik_list:
        klinik = csv.reader(klinik_list, delimiter=';')
        for each_klinik in klinik:
            kliniks.append({'nama_klinik': each_klinik[0], 'alamat': each_klinik[1], 'kota': each_klinik[2], 'provinsi': each_klinik[3], 'jam_buka': each_klinik[4], 'jam_tutup': each_klinik[5]})
    return kliniks

klinik = load_klinik()
for i in range(len(klinik)):
    LAYOUT_KLINIK.append(
        [   sg.Column([
            [sg.Text(klinik[i]['nama_klinik'], font='Any 20')],
            [sg.Text(klinik[i]['alamat'] + ', ' + klinik[i]['kota'] + ', ' + klinik[i]['provinsi']), sg.Text(klinik[i]['jam_buka'] + ' - ' + klinik[i]['jam_tutup'])],
            [sg.Button('Daftar')]], size=(920, 100), pad=BPAD_LEFT, visible=False, key=str(i))
        ])
