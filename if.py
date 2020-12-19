s1=0
s2=0
s3=0
s1=input("Birinci sayıyı gir: ")
s2=input("İkinci sayıyı gir: ")
s3=input("Üçüncü sayıyı gir: ")
enbuyuk=0
enkucuk=0
if int(s1) > int(s2):
    enkucuk=s2
    if int(s1) > int(s3):
        enbuyuk=s1
        if int(s3) < int(s2) :
            enkucuk=s3
    else:
        enbuyuk=s3
if int(s2) > int(s1):
    enkucuk=s1
    if int(s2) > int(s3):
        enbuyuk=s2
        if int(s3) < int(s1):
            enkucuk=s3
    else:
        enbuyuk=s3 

print("En büyük sayı: ",enbuyuk,"\nEn küçük sayı: ",enkucuk)
