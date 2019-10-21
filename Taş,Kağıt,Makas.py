import random
a = [1,2,3]
print("---------------------""\n"
      "---TAŞ,KAĞIT,MAKAS---""\n"
      "OYUNUNA HOŞ GELDİNİZ""\n"
      "---------------------")
oyuncu_puanı = 0
bilgisayar_puanı = 0
while True:
    print("1-Taş""\n"
          "2-Kağıt""\n"
          "3-Makas\n")
    try:
        oyuncu_seçimi = int(input("Seçiminizi yapın(3 olan kazanır)"))
    except:
        print("Sadece 1,2,3 girebilirsiniz")
        continue

    if(oyuncu_seçimi != 1 and oyuncu_seçimi != 2 and oyuncu_seçimi != 3):
        print("Hatalı sayı girdiniz")
        continue
    bilgisayar_seçimi = random.choice(a)



    if(oyuncu_seçimi ==1 and bilgisayar_seçimi == 1):
        print("Berabere,rakip de taş yaptı")
    if(oyuncu_seçimi ==1 and bilgisayar_seçimi == 2):
        print("Sen taş yaptın rakip kağıt yaptı,1 puan aldı")
        bilgisayar_puanı = bilgisayar_puanı + 1
    if(oyuncu_seçimi ==1 and bilgisayar_seçimi == 3):
        print("Sen taş yaptın rakip makas yaptı,1 puan aldın")
        oyuncu_puanı = oyuncu_puanı + 1
    if(oyuncu_seçimi ==2 and bilgisayar_seçimi == 1):
        print("Sen kağıt yaptın rakip taş yaptı,1 puan aldın")
        oyuncu_puanı = oyuncu_puanı + 1
    if(oyuncu_seçimi ==2 and bilgisayar_seçimi == 2):
        print("Berabere,rakip de kağıt yaptı")
    if(oyuncu_seçimi ==2 and bilgisayar_seçimi == 3):
        print("Sen kağıt yaptın rakip makas yaptı, 1 puan aldı")
        bilgisayar_puanı = bilgisayar_puanı + 1
    if(oyuncu_seçimi ==3 and bilgisayar_seçimi == 1):
        print("Sen makas yaptın rakip taş yaptı,1 puan aldı")
        bilgisayar_puanı = bilgisayar_puanı + 1
    if(oyuncu_seçimi ==3 and bilgisayar_seçimi == 2):
        print("Sen makas yaptın rakip kağıt yaptı,1 puan aldın")
        oyuncu_puanı = oyuncu_puanı + 1
    if(oyuncu_seçimi ==3 and bilgisayar_seçimi == 3):
        print("Berabere,rakip de makas yaptı")

    print("\n""DURUM""\nSen = {} Rakip =  {}\n".format (oyuncu_puanı,bilgisayar_puanı))



    if (oyuncu_puanı == 3):
        print("SEN KAZANDIN,TEBRİKLER")
        quit()
    if (bilgisayar_puanı == 3):
        print("RAKİP KAZANDI,BİR DAHAKİ SEFERE")
        quit()





