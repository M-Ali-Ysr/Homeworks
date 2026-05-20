import random

class Kart:
    def __init__(self, renk, sayi):
        self.renk = renk 
        self.sayi = sayi 

    def __str__(self):
        return f"{self.renk} {self.sayi}"

class Oyun:
    def __init__(self):
        self.renkler = ["Kırmızı", "Mavi", "Yeşil", "Sarı"]
        self.sayilar = ["0","1","2","3","4","5","6","7","8","9"]
        self.deste = []
        self.oyuncular = {}        
        self.oyuncu_listesi = []   
        self.siradaki_index = 0    
        self.ortadaki_kart = None  

    def deste_olustur(self):
        for renk in self.renkler:
            for sayi in self.sayilar:
                yeni_kart = Kart(renk, sayi)
                self.deste.append(yeni_kart)

        random.shuffle(self.deste)

    def oyunculari_al_ve_dagit(self):
        while True:
            sayi_input = input("Kaç kişi oynayacak? (En az 2): ")
            if sayi_input.isdigit() and int(sayi_input) >= 2:
                oyuncu_sayisi = int(sayi_input)
                break
            print("Hata: Lütfen en az 2 olacak şekilde bir sayı girin!")

        for i in range(1, oyuncu_sayisi + 1):
            while True:
                isim = input(f"{i}. Oyuncunun ismi ne olsun?: ").strip()
                if isim and isim not in self.oyuncular:
                    self.oyuncular[isim] = []
                    break
                print("Geçersiz veya zaten alınmış bir isim!")

        self.oyuncu_listesi = list(self.oyuncular.keys())

        for _ in range(5):
            for oyuncu in self.oyuncu_listesi:
                kart = self.deste.pop()
                self.oyuncular[oyuncu].append(kart)

        self.ortadaki_kart = self.deste.pop()

    def baslat(self):
        self.deste_olustur()
        self.oyunculari_al_ve_dagit()

        while True:
            siradaki_oyuncu = self.oyuncu_listesi[self.siradaki_index]
            mevcut_el = self.oyuncular[siradaki_oyuncu]

            print("\n" + "="*40)
            print(f"ORTADAKİ KART: [ {self.ortadaki_kart} ]")
            print(f"SIRA KİMDE: {siradaki_oyuncu}")
            print("="*40)

            print("Kartlarınız:")
            for i, kart in enumerate(mevcut_el, 1):
                print(f"{i}. {kart}")
            print("0. Pas Geç / Desteden Kart Çek")

            secim = input("\nOynamak istediğiniz kartın numarasını seçin: ")
            
            if not secim.isdigit() or int(secim) < 0 or int(secim) > len(mevcut_el):
                print("Geçersiz seçim! Lütfen listedeki numaralardan birini girin.")
                continue

            secim_index = int(secim)

            if secim_index == 0:
                if len(self.deste) > 0:
                    cekilen_kart = self.deste.pop()
                    mevcut_el.append(cekilen_kart)
                    print(f"\nDesteden şu kartı çektiniz: {cekilen_kart}")
                else:
                    print("\nDeste bitti, kart çekilemedi!")
                
                self.siradaki_index = (self.siradaki_index + 1) % len(self.oyuncu_listesi)
                continue

            secilen_kart = mevcut_el[secim_index - 1]

            if secilen_kart.renk == self.ortadaki_kart.renk or secilen_kart.sayi == self.ortadaki_kart.sayi:
                mevcut_el.remove(secilen_kart)
                self.ortadaki_kart = secilen_kart
                print(f"\n{siradaki_oyuncu}, '{secilen_kart}' kartını başarıyla oynadı.")

                if len(mevcut_el) == 0:
                    print("\n" + "*"*50)
                    print(f"TEBRİKLER! {siradaki_oyuncu} TÜM KARTLARINI BİTİRDİ VE KAZANDI! 🎉")
                    print("*"*50)
                    break  

                self.siradaki_index = (self.siradaki_index + 1) % len(self.oyuncu_listesi)
            else:
                print("\nHATA: Seçtiğiniz kart ortadaki kartla uyuşmuyor! (Renk veya Sayı aynı olmalı).")

oyun = Oyun()
oyun.baslat()