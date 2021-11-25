string = "ini string"
integer = 123

def check_data_type(kalimat,tebakan):
    tebakan = tebakan.lower()
    if (type(kalimat) == type(string)) and (tebakan == "str"):
        print("Jawaban anda benar")
        return "True"
    elif (type(kalimat) == type(integer)) and (tebakan == "int"):
        print("Jawaban anda benar")
        return "True"
    elif (type(kalimat) == type(integer)) and (tebakan == "str"):
        print("Jawaban anda salah, seharusnya adalah: int")
        return "False"
    elif (type(kalimat) == type(string)) and (tebakan == "int"):
        print("Jawaban anda salah, seharusnya adalah: str")
        return "False"
    else:
        print("Jawaban anda tidak valid")
        return "False"

print(check_data_type("Kevin","STr"))
print(check_data_type("Kevin","str"))
print(check_data_type(12345,"str"))
print(check_data_type("9347","int"))
print(check_data_type(9876,"int"))