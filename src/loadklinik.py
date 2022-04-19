import csv

def load_klinik():
    kliniks = []
    with open('src/data/klinik.txt') as klinik_list:
        klinik = csv.reader(klinik_list, delimiter=';')
        for each_klinik in klinik:
            kliniks.append({'nama_klinik': each_klinik[0], 'alamat': each_klinik[1], 'kota': each_klinik[2], 'provinsi': each_klinik[3], 'jam_buka': each_klinik[4], 'jam_tutup': each_klinik[5]})
    return kliniks

if __name__ == '__main__':
    klinik = load_klinik()
    print(klinik[1]['nama_klinik'])
    