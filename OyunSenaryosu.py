print("Uykudan uyandığında kendini bir ormanda buldun.Yatağında uyurken nasıl burada uynndığına anlam veremedin")
secim1 = int(input("1- Biraz etrafı dolaş""\n"
               "2- Olduğun yerde birinin seni bulmasını bekle"))
if(secim1 == 2):
    print("2 saattir kimse gelmedi ve gece olmaya başladı")
    secim2 = int(input("1- Bir barınak bul""\n"
                   "2- Beklemeye devam et""\n"))
    if(secim2 == 1):
        print("Geceleyin barınak aramak pek iyi bir fikir değil.Yürürken hava karanlık olduğundan"
              "oradaki yerlilerin tuazağını görmedin ve taşın altında ezildin")
        quit()
    if(secim2 == 2):
        print("Artık hava tamamen karardı ve kimse gelmedi.Etrafta hiç görmediğin yaratıklar göryorsun ve birden arkanda"
              " kocaman bir basilisk")
        secim3 = int(input("1- Ona yerde bulabildiğin ne varsa at""\n"
                       "2- Kaç"))
        if(secim3 == 1):
            print("Çabaların yetersiz kaldı basilisk seni tek hamlede öldürdü")
            quit()
        if(secim3 == 2):
            print("Kaçıyorsun ama kaçtığın yerde de birbirinden farklı yaratıklar var ve hepsi üstüne geliyor."
                  "Ama belkide bir şasın var.Yaratıkların olmadığı bir yer görüyorsun"
                  " orası denize gidiyor.")
            secim4 = int(input("1- Denize doğru koş""\n"
                           "2- Denizin içinde daha tehlikeli şeylerin olduğunu düşünüp orada kal"))
            if(secim4 == 2):
                print("Arkandan koşan 3 çeşit iskelet görünümlü yaratık seni yakalayıp öldürdüler,insanları sevmiyorlar")
                quit()
            if(secim4 == 1):
                print("Denizin kıyısında bir mağra var içine girdin ve o geceyi orada geçirdin.Sabah olduğunda")
                secim5 = int(input("1- Mağranın derinliklerine in""\n"
                                   "2- Dışarı çık "))
                if(secim5 == 2):
                    print("Gece evinde uyuduğun kaplan çıkışta seni bekliyordu."
                          "Daha olayın farkına varmadan öldün.")
                    quit()
                if(secim5 == 1):
                    print("Mağranın en altında 2 şey gördün: altın dolu bir kasa ve bir kılıç.İkisinide taşıyamazsın")
                    secim6 = int(input("1- Kılıcı al""\n"
                                       "2- Altınları al"))
                    if(secim6 == 2):
                        print("Elindeki altınlar seni geceleyin evinde uyuduğun kaplanın"
                              "saldırısından korumadı ")
                        quit()
                    if(secim6 == 1):
                        print("Kılıçla evinde uyuduğun kızgın kaplanın saldırısından kurtuldun,onu öldürdün"
                              "dışarı çıktığında da bir gemi gördün bu kurtuluş şansındı...")
                        print("KAZANDIN")

