import PySimpleGUI as sg
import csv

# Add some color to the window
theme_dict = {'BACKGROUND': '#2B475D',
                'TEXT': '#FFFFFF',
                'INPUT': '#F2EFE8',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#F2EFE8',
                'BUTTON': ('#000000', '#C2D4D8'),
                'PROGRESS': ('#FFFFFF', '#C7D5E0'),
                'BORDER': 1,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

sg.theme_add_new('Dashboard', theme_dict)
sg.theme('Dashboard')

BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT = ((10,20), (10, 20))

top_banner = [[sg.Text('Clinicare', font='Any 20', background_color=DARK_HEADER_COLOR)]]
top =	[[sg.Text("<< NAMA KLINIK >>", font="Any 20", key="TITLEKLINIK")],
    	 [sg.Text("<< 00:00 s/d 23.59 >>", key="JAMKLINIK")],
    	 [sg.Text("<< ALAMAT KLINIK >>", key="ALAMATKLINIK")]]

form = 	[[sg.Text('Dokter yang diinginkan', size=(30,1)), sg.Text(':', size=(1,1)), sg.Combo(['Dokter A', 'Dokter B', 'Dokter C'], key='COMBODOKTER', size=(20,1))],
		 [sg.Text('Tanggal Check Up', size=(30,1)), sg.Text(':', size=(1,1)), sg.Input('...-...-...', size=(10,1), key ="TANGGAL"), sg.CalendarButton('Pilih tanggal', target=(1,2),format='%Y-%m-%d')],
		 [sg.Text('Jam Check Up', size=(30,1)), sg.Text(':', size=(1,1)), sg.Spin([i for i in range(0,24)], initial_value=0, key='Hour'), sg.Spin([i for i in range(0,60)], initial_value=0, key='Minute')],
		 [sg.Text('Kontak yang bisa dihubungi', size=(30,1)), sg.Text(':', size=(1,1)),  sg.InputText(key='Kontak')],]


LAYOUT_PENDAFTARAN = 	[[sg.Column(top_banner, size=(960, 40), pad=(0,0), background_color=DARK_HEADER_COLOR)],
    					 [sg.Column(top, size=(920, 100))],
						 [sg.Column(form, size=(920, 120))],
						 [sg.Button('Back', key="BACKTOLIHAT"), sg.Button('Konfirmasi', key='KONFIRMASI')]
]

#def loadRegistrasiCheckUpLayout(nama_klinik,alamat_klinik,provinsi_klinik,kota_klinik,jam_buka,jam_tutup)

def getPasienFullName(username):
	with open('./src/data/Pasien.txt', encoding="UTF-8") as Pasien:
		pasienDB = csv.reader(Pasien, delimiter=',')
		for dataPasien in pasienDB:
			if dataPasien[0] == username:
				return dataPasien[1]
	return ''

def getKlinik(dokterFullName):
	with open('./src/data/Dokter.txt', encoding="UTF-8") as Dokter:
		dokterDB = csv.reader(Dokter, delimiter=',')
		for dataDokter in dokterDB:
			if dataDokter[1] == dokterFullName:
				return dataDokter[3]
	return ""

def getDokterByKlinik(klinik):
	listDokter = []
	with open('./src/data/dokter.txt', encoding="UTF-8") as Dokter:
		dokterDB = csv.reader(Dokter, delimiter=',')
		for dataDokter in dokterDB:
			if dataDokter[3] == klinik:
				listDokter.append(dataDokter[1])
	return listDokter
	
