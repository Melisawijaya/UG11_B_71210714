kalimat = str(input("Masukkan kalimat awal: "))
kalimatMasukan = str(input("Masukkan kata untuk disisipkan: "))
index = int(input("Masukkan index: "))

potongan = kalimat.find(kalimat[index-1])

print(kalimat[:potongan] + kalimatMasukan + kalimat[potongan:])