mahasiswa = [
    ["Andi", "Informatika", [75, 85, 90]],
    ["Budi", "Sistem Informasi", [65, 70, 60]],
    ["Citra", "Informatika", [95, 90, 100]],
    ["Dewi", "Sistem Informasi", [80, 85, 88]],
    ["Eka", "Teknik Komputer", [70, 72, 74]],
    ["Farhan", "Informatika", [60, 65, 70]]
]


def peringkat_global(data):
    ranking = []
    for mhs in data:
        nama = mhs[0]
        rata = sum(mhs[2]) / len(mhs[2])
        ranking.append((nama, rata))
    ranking.sort(key=lambda x: x[1], reverse=True)
    return [nama for nama, _ in ranking]

print("\nPeringkat Global:")
print(peringkat_global(mahasiswa))


