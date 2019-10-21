# Kelime Tahmin Oyunu
# Önce rastgele bir kelime seçilecek (Bu bir fonksiyon olsun. Bir listenin içinden rastgele bir kelime seçip versin)
# Kaç haklı oynamak istediğini oyuncuya soracak. 1 ile 25 arasında bir sayı seçmesi sağlanacak. Buna HakSayısı diyelim.
# Rastgele seçilen Kelimenin harf sayısı kadar ekrana ****** basılacak.
# ve Oyuncuya "Tahminini gir" diyecek. Bir harf girmek dışındaki girişlerde "hatalı giriş yaptın" diyecek.
# Girilen harf, kelienin içinde varsa onu görünür yapacak. "Tebrikler bir harf bildin. Kelime = ****A** " gibi bir mesaj vrecek
# Harf hatalı ise hakSayısından  düşecek.  Hak sayısı sıfır olunca "KAYBETTİN" mesajıyla oyun bitecek.
# Tahmin hakları bitmeden kelimeyi bilirse "TEBRİKLER KAZANDIN" mesajı ile oyun bitecek.
# kulanılacak kütüphane random
# mesela 1 ile 20 arasında rastgele bir sayı üretecek fonksiyon : randint(0,19)
#
# Her seferinde ekrana yıldızlı yazdırmak için ipucu :
# Tahmin girildiğinde, eğer girilen harf kelimenin içinde varsa bu harfi bulunanlar adlı bir diziye atarız
# kelimenin eleman sayısını len() ile buluruz.
# Bir döngüde her bir harf için şunu yaparız; bu harf bulunanlar dizisinde varsa harfin kendisini yazarız, yoksa * yazarız.
# En sonunda,
import random

#rastgele bir kelime bulma fonksiyonu
def KelimeSec():
    kelimeler = ['masa','kalemkutu','makas','ev','koyun','armut','kiraz','dolap','balina', "berat"]
    sayı = random.randint(0,len(kelimeler)-1)
    secim = kelimeler[sayı].lower()
    return secim



#tahmin edilecek kelimeyi yıldızlar halinde yazar. Bulunan harfleri yerlerine yerleştirir.
def EkranaYaz(kelime,liste):
    yazılacak = ""
    for harf in kelime:
        if (harf in liste):
            yazılacak = yazılacak + harf
        else:
            yazılacak = yazılacak + "*"

    print("KELİME = "+yazılacak)

    return yazılacak

#giriş ekranını gösteren fonksiyon
def GirisEkranı():
    print("-----KELİME TAHMİN OYUNUNA-----""\n"
          "-----------HOŞGELDİNİZ---------""\n"
          "-------------------------------""\n")

# burada, kullanıcı doğru bir seçim girene kadar soruluyor
def OyunHakSayısı():
    hak = 0
    while True:
        try:
            hak = int(input("Kaç haklı oynamak istersiniz."))
        except:
            print("Hatalı giriş yaptınız")
            continue
        if (hak > 25 or hak < 0):
            print("HATALI SEÇİM (1 ile 25 arasında seçim yapın) ")
            continue
        else:
            break
    return hak



# Programın ana bölümü

GirisEkranı()

kelime = KelimeSec()

uzunluk = len(kelime)

bulunan_harfler = []

oyunhakkı = OyunHakSayısı()

print("*" * uzunluk)

while True:

    harf = input("Harf tahmin edin")
    harf = harf.lower()
    if(harf in kelime):
        if(harf not in bulunan_harfler):
            bulunan_harfler.append(harf)
    else:
        oyunhakkı = oyunhakkı - 1
        print("{}  hakkınız kaldı. ".format(oyunhakkı))

    if (oyunhakkı == 0):
        print("Oyunu kaybettin")
        quit()

    ekranaYazılan = EkranaYaz(kelime,bulunan_harfler)

# eğer tüm harfler bulundu ise kazandın deyip oyunu bitirsin
    if(kelime == ekranaYazılan):
        print("Oyunu kazandınız TEBRİKLER")
        quit()




