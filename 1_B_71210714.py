def akarKubik(data):
    return data**(1/3)

def genap(data):
    if data%2==0:
        return akarKubik(data)
    else: 
        return "ganjil"

angka1=90
angka2=21
angka3=298745197907834587289340
print(genap(angka1))
print(genap(angka2))
print(genap(angka3))