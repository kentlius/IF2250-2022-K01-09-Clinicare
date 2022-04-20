import csv
import PySimpleGUI as sg

BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))

def get_request():
    requests = []
    with open("./src/data/jadwal.txt", encoding="utf-8") as request_list:
        request = csv.reader(request_list, delimiter=",")
        for each_request in request:
            requests.append({"dokter": each_request[1], "pasien": each_request[2], "kontak": each_request[5], "waktu": "Tanggal: "+each_request[3]+" Pukul: "+each_request[4], "klinik": each_request[0]})
    return requests

LAYOUT_CEK_JADWAL = [
        [sg.Column([[sg.Text('Clinicare', font='Any 20', background_color=DARK_HEADER_COLOR)]], size=(660, 40), pad=(0,0), background_color=DARK_HEADER_COLOR)],
        [sg.Column([[sg.Text('Jadwal Check-Up', font='Any 20', pad=((10,0), (0, 0)))]], size=(620, 50), pad=BPAD_TOP)],
]

for i in range(len(get_request())):
    LAYOUT_CEK_JADWAL.append([sg.Column([
                [sg.Text(get_request()[i]['username'], font='Any 20')],
                [sg.Text(get_request()[i]['kontak']), sg.Text(get_request()[i]['waktu']), sg.Text(get_request()[i]['klinik'])]],
                key='JADWAL'+str(i), visible=False, size=(450, 100), pad=BPAD_LEFT)])
