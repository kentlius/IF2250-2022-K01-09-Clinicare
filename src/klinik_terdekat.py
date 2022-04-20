import csv
import PySimpleGUI as sg
from style import DARK_HEADER_COLOR, BPAD_TOP, BPAD_LEFT

sg.theme('LightGreen3')

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
    with open('./src/data/klinik.txt', encoding="UTF-8") as klinik_list:
        klinik = csv.reader(klinik_list, delimiter=',')
        for each_klinik in klinik:
            kliniks.append({'nama_klinik': each_klinik[0], 'alamat': each_klinik[1], 'kota': each_klinik[2], 'provinsi': each_klinik[3], 'jam_buka': each_klinik[4], 'jam_tutup': each_klinik[5]})
    return kliniks

data_klinik = load_klinik()
for i in range(len(data_klinik)):
    LAYOUT_KLINIK.append(
        [   sg.Column([
            [sg.Text(data_klinik[i]['nama_klinik'], font='Any 20')],
            [sg.Text(data_klinik[i]['alamat'] + ', ' + data_klinik[i]['kota'] + ', ' + data_klinik[i]['provinsi']), sg.Text(data_klinik[i]['jam_buka'] + ' - ' + data_klinik[i]['jam_tutup'])],
            [sg.Button('Daftar')]], size=(920, 100), pad=BPAD_LEFT, visible=False, key=str(i))
        ])
