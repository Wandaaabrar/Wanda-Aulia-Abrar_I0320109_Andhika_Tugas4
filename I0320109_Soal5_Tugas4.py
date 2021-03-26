s = "geri menari di hutan"

#panjang harus 20
print("panjang dari s = %d" % len(s))

#huruf pertama 'a' harusnya di index no 8
print("kemunculan pertama a = %d" % s.index("a"))

#jumlah huruf a harusnya 2
print("a muncul sebanyak %d kali" % s.count("a"))

#memotong string berdasarkan index
print("lima karakter pertama adalah '%s'" % s[:5])
print("lima karakter berikutnya adalah '%s'" % s[5:10])
print("karakter ketiga belas adalah '%s'" % s[12])
print("karakter dengan index ganjil adalah '%s'" % s[1::2])
print("lima karakter terakhir adalah '%s'" % s[-5:])

#konversikan upercase
print("string dalam huruf besar: %s" % s.upper())

#konversikan ke lowercase
print("string dalam huruf kecil: %s" % s.lower())

#cek bagaimana string itu dimulai
if s.startswith("Str"):
    print("string dimulai dengan 'Str'. Good!")

#cek bagaimana string itu diakhiri
if s.endswith("ome!"):
    print("string diakhiri dengan 'ome!'. Good!")

#pisahkan string menjadi tiga string yang terpisah,
#masing-masing hanya berisi satu kata
print("pisahkan kata-kata dari string tersebut: %s" % s.split(" "))
