import PySimpleGUI as sg
import pandas as pd


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
top =	[[sg.Text("<< NAMA KLINIK >>", font="Any 20")],
    	 [sg.Text("<< 00:00 s/d 23.59 >>")],
    	 [sg.Text("<< ALAMAT KLINIK >>")]]

form = 	[[sg.Text('Dokter yang diinginkan', size=(30,1)), sg.Text(':', size=(1,1)), sg.Combo(['Dokter A', 'Dokter B', 'Dokter C'], key='Favorite Colour', size=(20,1))],
		 [sg.Text('Tanggal Check Up', size=(30,1)), sg.Text(':', size=(1,1)), sg.Input('...-...-...', size=(10,1), key ="date"), sg.CalendarButton('Pilih tanggal', target=(1,2),format='%Y-%m-%d')],
		 [sg.Text('Jam Check Up', size=(30,1)), sg.Text(':', size=(1,1)), sg.Spin([i for i in range(0,24)], initial_value=0, key='Hour'), sg.Spin([i for i in range(0,60)], initial_value=0, key='Minute')],
		 [sg.Text('Kontak yang bisa dihubungi', size=(30,1)), sg.Text(':', size=(1,1)),  sg.InputText(key='Kontak')],]


LAYOUT_PENDAFTARAN = 	[[sg.Column(top_banner, size=(960, 40), pad=(0,0), background_color=DARK_HEADER_COLOR)],
    					 [sg.Column(top, size=(920, 100))],
						 [sg.Column(form, size=(920, 120))],
						 [sg.Button('Back'), sg.Button('Konfirmasi')]
]

window = sg.Window('CLINICARE - Pendaftaran Check-Up', LAYOUT_PENDAFTARAN, background_color=BORDER_COLOR)
while True:
	event, values = window.read()
	print(event, values)
	if event == sg.WIN_CLOSED:
		break

window.close()
