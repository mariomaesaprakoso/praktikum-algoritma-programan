menu = {
    "nasi bakar":10000,
    "pecel lele":20000,
    "nasi padang":15000,
    "teh tawar/manis":5000,

}
print("=======selamat datang di restoran sederhana====")
username = input("masukan nama pesanan: ")
ttg = input("masukan alamat dan tanggal : ")

print(">>>>>>>>>>>>>>>>> ^ daftar menu ^ <<<<<<<<<<<<<<")
for i in menu :
    print("daftar menu :" ,i,"\t harga :",menu[i])
print("pembelian diatas Rp150.000,-mendapatkan diskon 5%")
print("=================================================")
beli = input("pilih menu : ")
jumlah =int(input("jumlah pesanan : "))
bayar = jumlah * menu[beli]

if bayar >150000 :
    diskon = bayar*15/100
    total = bayar - diskon
else:
    total = bayar

print("======== deatail pembayaran ======")
print("nama pemesan :",username)
print("menu di pesan : ",beli)
print("jumlah yang dipesan : ",jumlah)
print("alamat dan tanggal :",ttg)
print("total bayar : ",bayar)
print("terimakasih atas kunjungan anda ")