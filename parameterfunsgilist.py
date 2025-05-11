def cetak_nama(nama_list):
    for nama in nama_list:
        print(nama)

daftar_nama = ["Echa", "Tara", "Michael", "Nathaniel"]
cetak_nama(daftar_nama)


def hitung_rata_rata(angka_list):
    if len(angka_list) == 0:
        return 0
    return sum(angka_list) / len(angka_list)

nilai = [80, 90, 75, 85]
rata2 = hitung_rata_rata(nilai)
print("Rata-rata:", rata2)
