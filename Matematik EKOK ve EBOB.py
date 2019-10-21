# girilen iki sayının en küçük ortak katını bulacak.
# "... ve ... sayılarının EKOKu = ...." şeklinde sonucu söyleyecek.
# İPUCU : önce iki sayıdan hangisinin daha küçük olduğunu bulup, ordan başlanabilir.

sayı1 = int(input("bir sayı giriniz"))
sayı2 = int(input("bir sayı daha giriniz"))

sayac = 0
kucuksayı = 0
buyuksayı = 0
if(sayı1 > sayı2):
    buyuksayı = sayı1
    kucuksayı = sayı2
else:
    buyuksayı = sayı2
    kucuksayı = sayı1

while True:
    sayac = sayac + 1
    ekok = sayac*buyuksayı
    if(ekok%kucuksayı == 0):
        break

print("{} ve {} sayılarının ekoku = {}".format(sayı1,sayı2,ekok))

ebob = 1

for x in range(2,kucuksayı):
    while(buyuksayı % x == 0 and kucuksayı % x == 0):
        ebob = ebob*x
        buyuksayı = buyuksayı/x
        kucuksayı = kucuksayı/x
print("{} ve {} sayılarının ebobu = {}".format(sayı1,sayı2,ebob))