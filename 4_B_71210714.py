kalimat = str(input("Masukkan kalimat untuk dihitung: "))
 
def hitung():
    totalhuruf = len(kalimat)
    perhitunganhuruf = 2/3
    hasilpembulatan = totalhuruf * perhitunganhuruf
    return hasilpembulatan

kata = hitung()
print (int(kata))