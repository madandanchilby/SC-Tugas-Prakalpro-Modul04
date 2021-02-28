#Kalkulator Bangun Datar adalah hasil dari pengembangan kalkulator sederhana yang biasa
#kita jumpai dalam kehidupan sehari-hari. Di dalam Kalkulator Bangun Datar terdapat
#beberapa fitur terbaru yang menarik dan memudahkan kita dalam melakukan penghitungan
#luas beberapa bangun datar. Berikut fitur-fitur yang disediakan Kalkulator Bangun Datar:
#1. Menghitung luas segitiga.
#2. Menghitung luas lingkaran.
#3. Menghitung luas trapesium.
#Buatlah program Kalkulator Bangun Datar dengan ketentuan setiap fungsi hanya bisa
#menghitung satu fitur, maka anda membutuhkan minimal 3 fungsi untuk membuat fitur-fitur
#tersebut.
#Silahkan anda menggunakan template fungsi berikut ini dengan catatan, Anda tidak
#diperbolehkan mengubah nama fungsi dan tidak diperbolehkan menambahkan atau
#mengurangi jumlah parameter yang ada dalam template fungsi dibawah ini.
#def segitiga(alas,tinggi):

#def lingkaran(jari):

#def trapesium(sisiPendek, sisiPanjang, tinggi):


print('===== Kalkulator Bangun datar=====')
print('Pilih Menu Kalkulator Bangun Datar')
print('1.segitiga')
print('2.Lingkaran')
print('3.Trapesium')
pilih=int(input('masukan pilihan='))
if 0 < pilih < 4:
    if pilih == 1:
        def segitiga (alas,tinggi):
            Luas=0.5 * alas * tinggi
            return Luas
        alas=int(input('masukan alas='))
        tinggi=int(input('masukan tinggi='))
        Luas_segitiga=segitiga(alas,tinggi)
        print('luas segitiga=',Luas_segitiga)
    elif pilih ==2:
        def lingkaran(jari):
            Luas=3.14 * jari**2
            return Luas
        jari=int(input('masukan jari-jari='))
        Luas_lingkaran=lingkaran(jari)
        print('luas Lingkaran=',Luas_lingkaran)
    elif pilih==3:
        def trapesium (sisiPendek,sisiPanjang,tinggi):
            Luas=0.5 * (sisiPendek+sisiPanjang)*tinggi
            return Luas
        sisiPendek=int(input('masukan sisi pendek='))
        sisiPanjang=int(input('masukan sisi panjang='))
        tinggi=int(input('masukan tinggi='))
        Luas_trapesium=trapesium (sisiPendek,sisiPanjang,tinggi)
        print('Luas Trapesium=',Luas_trapesium)
