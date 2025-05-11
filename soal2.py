def hitung_rata_rata():
    angka_list = []

    while True:
        inp = input("Masukkan bilangan (atau ketik 'done' untuk selesai): ")
        
        if inp.lower() == "done":
            break
        
        try:
            angka = float(inp)
            angka_list.append(angka)
        except ValueError:
            print("Input tidak valid! Masukkan angka atau 'done'.")

    if len(angka_list) == 0:
        print("Tidak ada bilangan yang dimasukkan.")
    else:
        rata_rata = sum(angka_list) / len(angka_list)
        print("Rata-rata dari bilangan yang dimasukkan adalah:", rata_rata)
