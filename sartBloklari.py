#Bir bankanın kredi hesaplama makinası
krediCesitleri=["HızlıKredi","Maaşını Halkbank'tan Alanlara Özel Kredi","Mutlu Emeklilik İhtiyaç Kredisi","Kamu Çalışanlarına Özel Kredi","Özel Sektör Çalışanlarına Özel Kredi"]
faizMiktarlari=[1.44,1.36,1.39,1.41,1.77]

girilenKredi=input(" Seçmek istediğiniz kredi çeşitini giriniz: ")
girilenTutar=int(input("Lütfen ihtiyacınız olan kredi miktarını giriniz: "))

#list içerisindeki hangi krediyi seçtiyse onu indis değeri olarak krediNumarasi adlı değişkene  aldım
sayac=0
krediNumarasi=0
for i in krediCesitleri:
    if girilenKredi==i:
        krediNumarasi=sayac
        print(krediNumarasi)
    sayac+=1

#Seçilen kredi ve istenilen tutara göre sabit faiz oranları ile çarparak kredi miktarı hesaplandı
krediHesapla=0
if  krediNumarasi==0 :
    krediHesapla=girilenTutar*faizMiktarlari[4]
if krediNumarasi==1 and girilenTutar<10000:
    krediHesapla=girilenTutar*faizMiktarlari[3]
else:
    krediHesapla=girilenTutar*faizMiktarlari[0]
if krediNumarasi==2:
    krediHesapla=girilenTutar*faizMiktarlari[2]
if krediNumarasi==3 and girilenTutar<10000:
    krediHesapla=girilenTutar*faizMiktarlari[1]
else:
    krediHesapla=girilenTutar*faizMiktarlari[2]
if krediNumarasi==4 and girilenTutar<10000:
    krediHesapla=girilenTutar*faizMiktarlari[0]
else:
    krediHesapla=girilenTutar*faizMiktarlari[2]
    
print("Sizin isteklerinize uygun olarak hesaplanan kredi tutarınız: ",krediHesapla)