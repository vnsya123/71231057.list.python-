def tiga_terbaik(data):
    data_terurut = sorted(data, reverse=True)
    return data_terurut[:3]
angka = [45, 67, 89, 12, 90, 33, 100]
hasil = tiga_terbaik(angka)
print("3 bilangan terbaik:", hasil)



