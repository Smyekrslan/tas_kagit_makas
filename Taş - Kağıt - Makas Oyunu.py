import random

#Oyun Tanıtımı
def tas_kagit_makas_SÜMEYYE_KARAASLAN():
  print("Taş, Kağıt, Makas Oyununa Hoş Geldiniz!")
  print("Oyunun Kuralları : Taş makası yener; makas kağıdı yener; kağıt taşı yener.")
  print("İlk 2 turu kazanan oyunun galibi olur. Oyundan çıkmak için q tuşuna basın.")

  #Oyun Kurulumu
  secenekler = ["taş", "kağıt", "makas"]

  while True:
    oyuncu_galibiyeti = 0
    bilgisayar_galibiyeti = 0
    oynanan_tur_sayisi = 0


    while oyuncu_galibiyeti < 2 and bilgisayar_galibiyeti < 2 :
      oyuncu_secimi = input("\nTaş, kağıt veya makas seçin: ").lower()
      if oyuncu_secimi == "q":
        print("Oyun bitti. Teşekkürler!")
        return


      if oyuncu_secimi not in secenekler :
        print("Geçersiz seçim. Lütfen taş, kağıt veya makas girin.")
        continue

      #Bilgisayarın seçimi rastgele yapması
      bilgisayar_secimi = random.choice(secenekler)
      print(f"Bilgisayarın seçimi : {bilgisayar_secimi}")

      #Kazananı Belirleme
      if oyuncu_secimi == bilgisayar_secimi:
        print("Bu tur berabere!")

      elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
           (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
           (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
        print("Bu turu kazandınız!")
        oyuncu_galibiyeti += 1

      else:
        print("Bu turu kaybettiniz!")
        bilgisayar_galibiyeti += 1

        oynanan_tur_sayisi += 1

    #Oyunun Galibini Belirleme(2 Turu da kazanan galip olur.)
    if oyuncu_galibiyeti == 2 :
      print("Tebrikler! oyunu kazandınız!")

    else:
      print("Bilgisayar oyunu kazandı!")

    #Devam etme sorusunun sorulması
    devam_mi = input("\nBir oyun daha oynamak ister misiniz? (evet/hayır) : ").lower()
    bilgisayar_devam_mi = random.choice(["evet", "hayır"])
    print(f"Bilgisayar devam etmek istiyor mu? : {bilgisayar_devam_mi}")

    if devam_mi == "evet" and bilgisayar_devam_mi == "evet":
      print("\nOyun tekrar başlıyor...")

    else :
      print("Oyun sona erdi. Teşekkürler!")
      break


tas_kagit_makas_SÜMEYYE_KARAASLAN()
