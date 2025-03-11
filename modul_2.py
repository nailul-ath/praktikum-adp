print ('Halo! selamat datang di math cafe, \nsilakan pilih paket pesanan anda!')

#pemilihan paket
paket_1 = 'ayam = Rp20000'
paket_2 = 'sapi = Rp35000'
paket_3 = 'cumi-cumi = Rp45000'
print (f'paket 1 : {paket_1} \npaket 2 : {paket_2} \npaket 3 : {paket_3}')
pilihan= int(input('pilihan paket pesanan anda [1/2/3]: '))
jumlah= int(input('jumlah pesanan anda               : '))
if pilihan == 1:
    harga = 20000
elif pilihan ==2:
    harga= 35000
elif pilihan ==3:
    harga= 45000
else:
    print ('mohon pilih paket yang telah disediakan')

total= harga*jumlah

#ongkos kirim
jarak = float(input('jarak rumah anda ke restoran(km)  : '))
if jarak<1:
    ongkir = 0
elif 1<=jarak<=3:
    ongkir = 7000
else:
    ongkir = 15000

#struk pembayaram
print('-------------------------------------------------')
print (f'total harga pesanan anda           : Rp{total}')
print (f'ongkos kirim anda                  : Rp{ongkir}')

total_akhir= total+ongkir
print (f'total harga yang perlu anda bayar  : Rp{total_akhir}')
print('-------------------------------------------------')
print('terimakasih sudah memesan di math cafe\nsilakan tunggu makanan anda!')
