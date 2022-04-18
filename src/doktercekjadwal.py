import PySimpleGUI as sg

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

top  = [[sg.Text('Klinik Terdekat', font='Any 20', pad=((10,0), (0, 0)))]]

block_3 = [[sg.Text('Nama Klinik', font='Any 20')],
            [sg.Text('Alamat Klinik'), sg.Text('Jam Buka & Tutup')],
            [sg.Button('Daftar')]]

block_2 = [[sg.Text('Nama Klinik', font='Any 20')],
            [sg.Text('Alamat Klinik'), sg.Text('Jam Buka & Tutup')],
            [sg.Button('Daftar')]]

block_4 = [[sg.Text('Nama Klinik', font='Any 20')],
            [sg.Text('Alamat Klinik'), sg.Text('Jam Buka & Tutup')],
            [sg.Button('Daftar')]]

block_5 = [[sg.Text('Nama Klinik', font='Any 20')],
            [sg.Text('Alamat Klinik'), sg.Text('Jam Buka & Tutup')],
            [sg.Button('Daftar')]]

LAYOUT_KLINIK = [[sg.Column(top_banner, size=(960, 40), pad=(0,0), background_color=DARK_HEADER_COLOR)],
          [sg.Column(top, size=(920, 50), pad=BPAD_TOP)],
          [sg.Column([[sg.Column(block_2, size=(450,100), pad=BPAD_LEFT_INSIDE)],
                      [sg.Column(block_3, size=(450,100),  pad=BPAD_LEFT_INSIDE)]], pad=BPAD_LEFT, background_color=BORDER_COLOR),
           sg.Column([[sg.Column(block_4, size=(450,100), pad=BPAD_LEFT_INSIDE)],
                      [sg.Column(block_5, size=(450,100), pad=BPAD_LEFT_INSIDE)]], pad=BPAD_LEFT, background_color=BORDER_COLOR)]]