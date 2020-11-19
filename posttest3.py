
print("==============================")
print("  SELAMAT DATANG DI TOKO SULE ")
print("==============================")
print(" \t menu")
print("------DAFTAR PILIHAN KUE------")
print("==============================")
print("1. Kue keju  \n-untuk pembelian 4-15 pcs diskon 10% \n-untuk pembelian 16-25 pcs diskon 15%")
print("2. Kue coklat \n-untuk pembelian 5-20 pcs diskon 7% \n-untuk pembelian 21-35 pcs diskon 12%")
print("3. Keluar")
menu = int(input("Masukkan pilihan kue: "))
if menu == 1:
    harga = 6000
    print("harga 1 kue: ", str(harga))
    jumlah = int(input("Masukkan jumlah kue: "))
    total = harga*jumlah
    if 3 < jumlah < 16:
        diskon = total*(10/100)
        print("diskon: Rp. %d" % (diskon))
        print("total belanja: Rp. %d" % (total-diskon))
        bayar = float(input("bayar: Rp. "))
        total1 = total-diskon
        if bayar >= total1:
            print("kembalian: Rp. %d" % (bayar-total1))
        else:
            print("uang anda kurang")
    elif 15 < jumlah < 26:
        diskon = total*(15/100)
        print("diskon: Rp. %d" % (diskon))
        print("total belanja: Rp. %d" % (total-diskon))
        bayar = float(input("bayar: Rp. "))
        total1 = total-diskon
        if bayar >= total1:
            print("kembalian: Rp. %d" % (bayar-total1))
        else:
            print("uang anda kurang")
    else:
        print("jumlah kue tidak termasuk harga diskon")
        print("total belanja: Rp. %d" % (total))
        bayar = float(input("bayar: Rp. "))
        if bayar >= total:
            print("kembalian: Rp. %d" % (bayar-total))
        else:
            print("uang anda kurang")
elif menu == 2:
    harga = 3500
    print("harga 1 kue: ", str(harga))
    jumlah = int(input("Masukkan jumlah kue: "))
    total = harga*jumlah
    if 4 < jumlah < 21:
        diskon = total*(7/100)
        print("diskon: Rp. %d" % (diskon))
        print("total belanja: Rp. %d" % (total-diskon))
        bayar = float(input("bayar: Rp. "))
        total1 = total-diskon
        if bayar >= total1:
            print("kembalian: Rp. %d" % (bayar-total1))
        else:
            print("uang anda kurang")
    elif 20 < jumlah < 36:
        diskon = total*(12/100)
        print("diskon: Rp. %d" % (diskon))
        print("total belanja: Rp. %d" % (total-diskon))
        bayar = float(input("bayar: Rp. "))
        total1 = total-diskon
        if bayar >= total1:
            print("kembalian: Rp. %d" % (bayar-total1))
        else:
            print("uang anda kurang")
    else:
        print("jumlah kue tidak termasuk harga diskon")
        print("total belanja: Rp. %d" % (total))
        bayar = float(input("bayar: Rp. "))
        if bayar >= total:
            print("kembalian: Rp. %d" % (bayar-total))
        else:
            print("uang anda kurang")
elif menu== 3:
    keluar=input("Anda yakin ingin keluar?(y/t): ")
    if keluar=="y":
        print("keluar")
        exit()
else :
    print("pilihan tidak ditemukan, silahkan ulangi")


