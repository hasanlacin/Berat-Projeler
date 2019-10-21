"""
İki oyunculu bir oyun
Önce ilk oyuncunun adını alacak. (Boş olamaz, boş olursa tekrar isteyecek) (Mesela BERAT)

Sonra ikinci oyuncunun adını soracak. (Boş olamaz,)
 ve ilk oyuncunun adını alırsa "Bu isim daha önce alınmış" diyip yine isteyecek (MESELA HASAN)

 Sonra kimin oyuna başlayacağını belirlemek için program rastgele seçim yapacak. (yazı tura gibi)

 Kimin başlayacağını belirledikten sonra "HASAN oyuna başlayacak" diye mesaj verecek.

 Oyunun başında her iki oyuncunun da 100 sağlığı var. Şu şekilde gösterecek :

 HASAN                                                       BERAT
 HP:100 ||||||||||||||||||||||||||||||||||||||||||||||||||  HP:100 ||||||||||||||||||||||||||||||||||||||||||||||||||

 Sonra saldırılar başlıyor, :
 "HASAN saldırıyor"
 "Lütfen saldırı gücünü giriniz (1-50 arası):" diye soracak.
 Oyuncu sıfır girerse veya 50den büyük bir sayı girerse "Lütfen 1 ile 50 arası bir sayı giriniz" diyecek.
 Saldırı gücünü aldıktan sonra hamlenin başarılı olup olmadığına karar verecek:
 Oyuncu ne kadar yüksek bir güç seçmiş ise başarılı olma şansı o kadar düşecek.
Örneğin 40 dedi ise 100-40 = %60 başarı şansı olacak. 10 dedi ise 100-10=%90 başarı şansı olacak.

 Hamle başarılı olursa :
  "HASAN 30 puanlık hasar verdi" gibi mesaj verecek ve diğer oyuncunun sağlığından o kadar düşecek.
Hamle başarısız olursa :
 "HASAN Hamleyi kaçırdı" mesajı verecek.
 Ardından yine sağlık durumunu gösterecek.
(Sağlık durumunu göstermek için bir fonksiyon olsun. gerektikçe bu fonksiyonu çağıralım)


 Sonra sıra diğer oyuncuya geçer ve "HASAN saldırıyor" mesajı yerine "BERAT saldırıyor" diyerek tekrar başlayacak.

  Oyunculardan birinin sağlığı sıfır veya altına düşerse oyun bitecek.

 " ************** Oyunu BERAT kazandı!!!***************" gibi bir mesaj verecek.

  Ardından "Tekrar oynamak ister misiniz (E/H)" diye soracak ve E denirse yazı tura atımına kadar oyun başa dönecek.
  H denirse program bitecek.

"""



