
class kandang:
    def __init__(self, kandang):
        self.kandang = kandang

p1 =kandang("kandang buaya : Rp 100000")
p2 =kandang("kandang anaconda : Rp 20000")
p3 =kandang("kandang komodo : Rp 1000000")
p4 =kandang("kandang harimau : Rp 10000000")

print('selamat datang di kebun binatang kami')
while True:
    print('kandang yang ingin di kunjungi')
    print('1.kandang buaya')
    print('2.kandang anaconda')
    print('3.kandang komodo')
    print('4.kandang harimau')

    kandang = int(input('pilih kandang: '))
    jumlahpesan=int(input("masukan jumlah pesanan: "))

    if kandang == 1:
        print(p1.kandang)
        harga = 100000 * jumlahpesan
        print("total yang harus dibayar Rp." +str(harga))

    elif kandang == 2:
        print(p2.kandang)
        harga = 20000 * jumlahpesan
        print("total yang harus di bayar Rp." +str(harga))
   
    elif kandang == 3:
        print(p3. kandang)
        harga = 1000000 * jumlahpesan
        print("total yang harus di bayar Rp." +str(harga))
    elif kandang == 4:
        print(p4.kebunbinatang)
        harga = 10000000 * jumlahpesan
        print("total yang harus di bayar Rp." +str(harga))

        print("_______________")
        print("hewan buas")
        print("_______________")
        print("jumlah pengunjung :")
        print("___________________")
        print("jumlah bayar :", harga)
        print("_________________")
        pilihan=input("apakah sudah puas Y/T =")
    
    



