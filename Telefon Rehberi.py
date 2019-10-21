# Program en başta bir defa bir açılış ekranı göstersin.
#  **********************************************************
#  *********  TELEFON REHBERİ ******************************
#  *********  Oluşturan : Berat Laçin **********************
#  *********************************************************
#
# program bir menü gösterecek.
# 1 - Rehbere Kayıt Ekle
# 2 - Bilgileri Listele
# 3 - Telefon Numarası Arama
# 4 - Kaydet
# 5 - Çıkış
# Seçiminizi giriniz :
# ----------------------------------------------------------
#  Bilgi Gir Kısmı
# İsim Giriniz diyerek ismi alacak, Telefonunu giriniz diyerek takım bilgisini alacak.
# Ve aldığı bilgiyi bir "dictionary" sözlüğe kaydedecek. Sonra yine ana menüyü gösterecek.
#  Bilgileri Listele Kısmı
# Sözlüğümüzdeki her bir satırı şu şekilde ekrana basacak :
#  İSİM : AAAAAAAAAA
#  TELEFON : XXXXXXXXXXX
#  Sonra yine ana menüyü gösterecek
# 3 girilise, bir isim isteyecek ve girilen kişinin Telefon numarasını bulup ekrana yazdıracak.
# 4 girilirse, sözlüğün o sıradaki halini, dosyaya yazsın. (rehber.txt dosyası)
# 5 girilirse program biter.

Rehber = {}

def RehbereKayıtEkleme():
    cevap = "e"
    while(cevap == "e"):
        isim = input("isminizi girin")
        numara = input("numaranızı girin")
        Rehber[isim] = numara
        cevap = input("farklı isim girmek istiyor musun(e/h)")

def  RehberKayıtlarınıListeleme():
    for sıradaki in Rehber:
        print("İsim = {}\nNumara = {}".format(sıradaki,Rehber[sıradaki]))
        print("-----------------------------")



def TelefonNumarasıArama():

    arama = input("kimin numarasını aramak istersiniz")
    if(arama in Rehber):
        print("\n{} adlı kişinin telefon numarası = {}".format(arama,Rehber[arama]))
        print("---------------------------------------")
    else:
        print("rehberde öyle bir isim yok")

def DosyayaKaydetme():
    print("YAKINDA")



print("****************************\n"
      "*******Telefon Rehberi******\n"
      "****************************")
#öncelikle, kayıtlı numaraları alıp sözlüğümüze ekliyoruz.


while True:
    print("\n")
    print("1- Rehbere Kayıt Ekle")
    print("2- Rehber Kayıtlarını Listele")
    print("3- Telefon Numarası Arama")
    print("4- Dosyaya Kaydetme")
    print("5- Çıkış")
    print("\n")
    
    try:
        seçim = int(input("yapmak istediğiniz işlemi seçin"))
    except:
        print ("\nHatalı giriş yaptınız")
        continue
        
    if(seçim == 1):
        RehbereKayıtEkleme()
    elif(seçim == 2):
        RehberKayıtlarınıListeleme()
    elif(seçim == 3):
        TelefonNumarasıArama()
    elif(seçim == 4):
        DosyayaKaydetme()
    elif(seçim == 5):
        quit()
    else:
        print("Hatalı sayı girdiniz")










3
