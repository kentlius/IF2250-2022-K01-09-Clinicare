import csv
import PySimpleGUI as sg

BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)

def get_request():
    requests = []
    with open("./test/jadwal_checkup.txt", encoding="utf-8") as request_list:
        request = csv.reader(request_list, delimiter=",")
        for each_request in request:
            requests.append({"username": each_request[0], "kontak": each_request[1], "waktu": each_request[2], "klinik": each_request[3]})
    return requests

def delete_request(delete):
    requests = []
    with open("./test/jadwal_checkup.txt", encoding="utf-8") as request_list:
        request = csv.reader(request_list, delimiter=",")
        for each_request in request:
            if (delete['username'] != each_request[0] or delete['kontak'] != each_request[1] or delete['waktu'] != each_request[2] or delete['klinik'] != each_request[3]):
                requests.append({"username": each_request[0], "kontak": each_request[1], "waktu": each_request[2], "klinik": each_request[3]})
    with open("./test/jadwal_checkup.txt", "w", encoding="utf-8") as request_list:
        request = csv.writer(request_list, delimiter=",", lineterminator="\n")
        for each_request in requests:
            request.writerow([each_request["username"], each_request["kontak"], each_request["waktu"], each_request["klinik"]])

LAYOUT_CEK_JADWAL = [
        [sg.Column([[sg.Text('Clinicare', font='Any 20', background_color=DARK_HEADER_COLOR)]], size=(960, 40), pad=(0,0), background_color=DARK_HEADER_COLOR)],
        [sg.Column([[sg.Text('Daftar Request', font='Any 20', pad=((10,0), (0, 0)))]], size=(920, 50), pad=BPAD_TOP)],
]

for i in range(len(get_request())):
    LAYOUT_CEK_JADWAL.append([sg.Column([
                [sg.Text(get_request()[i]['username'], font='Any 20')],
                [sg.Text(get_request()[i]['kontak']), sg.Text(get_request()[i]['waktu']), sg.Text(get_request()[i]['klinik'])],
                [sg.Button('Terima', key="MAIN_CONFIRM"+str(i)), sg.Button('Tolak', key="MAIN_REJECT"+str(i))]], 
                key='REQUEST'+str(i), visible=False, size=(450, 100), pad=BPAD_LEFT)])
