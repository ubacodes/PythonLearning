#dictionary konusu 
#indis olayı yoktur anahtar kelimelerle erişim oluyor o yüzden sıralı tutulmaz
sozluk1 = {"bir":1,"iki":2,"üç":3}

sozluk2 = {}

sozluk1["beş"] = 5 #sozluklere eleman ekleme
a = {"bir":[1,2,3,4],"iki":[[1,2],[3,4],[5,6]]}
print(a["bir"], "and ",a["iki"])

print(a.keys()) #dict ler içerisindeki anahtarları alıyoruz sadece valuesler hariç
print(a.items()) #dict içerisindeki verileri tuple olarak alıyoruz normalde dizi şeklinde tutuyor

#for döngüsü ile kullanımı burada tuple olarak aldık içerisindeki değerler hakkında
#işlem yapamayız ama for ile sıralı olarak yazdırabiliriz.
for k,v in a.items() :
    print(k,v)