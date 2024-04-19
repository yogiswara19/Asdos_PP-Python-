
# a = "UcuP ganTeng"
# print(a.lower())

# b = "   Dadang galau "
# print(b.strip())

# c = "Hari libur Natal"
# print(c.replace("Natal", "Lebaran"))

# d = "Bapak Budi baik"
# print(d.split())

class Kucing:
    def __init__(self, warna, usia):
        self.warna = warna
        self.usia = usia

    def bersuara(self):
        print(f"Meow!, Kucing ini berwarna {self.warna} dan berusia {self.usia} tahun")

kucing_kesayangan = Kucing(warna="putih", usia=1)

kucing_kesayangan.bersuara()

