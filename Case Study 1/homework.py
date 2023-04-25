# verilen değerlerin veri yapılarını inceleyin

x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"name" : "jake",
     "age" : 27,
     "adress" : "Downtown"}
t = ("machine learning", "data science")
s = {"python", "machine learning", "Data science"}

type(x)
type(y)
type(z)
type(a)
type(b)
type(c)
type(l)
type(d)
type(t)
type(s)

# Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.
# Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insight."
text.upper().replace(".", " ").replace(",", " ").split()
print(text)

# Verilen listeye aşağıdaki adımları uygulayınız

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Adım 1: Verilen listenin eleman sayısına bakınız.
len(lst)
# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
lst[0]
lst[10]
# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
lst[0:4]
# Adım 4: Sekizinci indeksteki elemanı siliniz.
lst.pop(8)
# Adım 5: Yeni bir eleman ekleyiniz.
lst.append("A")
# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
lst.insert(8, "N")
lst

# Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 22],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

# Adım 1: Key değerlerine erişiniz.
dict.keys()
# Adım 2: Value'lara erişiniz.
dict.values()
# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict["Daisy"][1] = 13
# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict.update({"Ahmet": ["Turkey", 24]})
# Adım 5: Antonio'yu dictionary'den siliniz.
dict.pop("Antonio")

# Arguman olarak bir liste alan,
# listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan
# ve bu listeleri return eden fonskiyon yazınız.

l = [2,13,18,93,22]

def listele(list) :
     even_number = []
     odd_number = []

     for i in list:
          if i % 2 == 0:
               even_number.append(i)
          else:
               odd_number.append(i)
     return even_number, odd_number

listele(l)

# Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
# bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
# tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for index, ogrenci in enumerate(ogrenciler):
     if index<3:
          index += 1
          print("Mühendislik Fakültesi", index, "Öğrenci: ", ogrenci)
     else:
          index -=2
          print("Tıp fakültesi", index, "Öğrenci: ", ogrenci)

#  Aşağıda 3 adet liste verilmiştir.
# Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır.
# Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
     print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")

#  Aşağıda 2 adet set verilmiştir.
#  Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
# eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak
# fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume(set1, set2):
     if set1.issuperset(set2):
          print(set1.intersection(set2))
     else:
          print(set2.difference(set1))
kume(kume1,kume2)
kume(kume2, kume1)


















