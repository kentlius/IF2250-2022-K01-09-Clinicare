from klinik_terdekat import load_klinik

def test_1():
    list_of_klinik = load_klinik()

    assert len(list_of_klinik) > 0
