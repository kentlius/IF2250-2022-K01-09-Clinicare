# IF2250-2022-K01-09-Clinicare

Permasalahan yang sering timbul saat ini adalah kesusahan seseorang dalam melakukan check-up kesehatan karena rumah sakit/klinik yang antri, susah menemukan jadwal yang cocok dengan dokter, proses administrasi yang cukup rumit sehingga sebagian orang malas untuk melakukan check-up tersebut karena merasa terbebani dengannya, dan lain sebagainya. Oleh karena itu, dibutuhkan suatu sistem yang mempermudah urusan tersebut sehingga orang-orang tidak akan mengalami kesusahan lagi. Sistem tersebut adalah aplikasi check-up kesehatan yang bernama Clinicare. Dengan adanya aplikasi tersebut maka pasien yang hendak melakukan check-up kesehatan akan dimudahkan dengan adanya fitur penjadwalan check-up secara online (dapat memilih klinik yang terdekat dan dokter yang diinginkan), konsultasi online, dan tersedianya riwayat dan hasil check-up sebelumnya.

## Instalasi

```sh
pip install pysimplegui
```

## Cara Menjalankan Aplikasi

```sh
cd src
py main.py
```

## Daftar Modul

### Login & Register

Penanggung Jawab: 13520025 - Fransiskus Davin Anwari
![Login](/doc/login.png)
![Registrasi](/doc/registrasi.png)

### Klinik Terdekat

Penanggung Jawab: 13520069 - Kent Liusudarso
![Klinik Terdekat](/doc/klinik.png)

### Registrasi Check Up

Penanggung Jawab: 13520079 - Ghebyon Tohada Nainggolan
![Check Up](/doc/checkup.png)

### Dokter Cek Jadwal

Penanggung Jawab: 13520067 - Farnas Rozaan Iraqee
![Cek Jadwal](/doc/jadwal.png)

## Daftar Tabel Basis Data

| User       |
| ---------- |
| _Username_ |
| Password   |
| Tipe       |

| Klinik       |
| ------------ |
| _NamaKlinik_ |
| Alamat       |
| JamBuka      |
| JamTutup     |
