"""import random
#import string
colors = ["Red","Blue","Green","Yellow"]
numbers = [str(i) for i in range(10)#,"Pass","+2","Direction"
           ]

tuple = []
for color in colors:
    for number in numbers:
        tuple.append(f"{color} {number}")

random.shuffle(tuple)

players = {
    "Player 1": [],
    "Player 2": []
}

for _ in range(7):
    for player in players:
        players[player].append(tuple.pop())

the_card_in_the_middle = tuple.pop()

the_next_player = "Player 1"

while True:
    print("\n" + "="*40)
    print(f"Ortadaki kart: [{the_card_in_the_middle}]")
    print(f"Sıra Kimde: {the_next_player}")
    print("="*40)

    current_round = players[the_next_player]
    print("Your Cards: ")
    for i, card in enumerate(current_round,1):
        print(f"{i}. {card}")
    print(f"0. Pas Geç / Desteden Kart Çek")

    election = input("\nOynamak İstediğiniz kartın numarasını seçin: ")

    if not election.isdigit() or int(election) < 0 or int(election) > len(current_round):
        print("Geçersiz bir seçim yaptınız, lütfen tekrar deneyin.")
        continue

    election_index = int(election)

    if election_index == 0:
        if len(tuple) > 0:
            drawn_card = tuple.pop()
            current_round.append(drawn_card)
            print(f"\nDesteden bir kart çektiniz: {drawn_card}")
        else:
            print("\nDeste Bitti! kart çekemiyorsunuz, pas geçildi.")
        
        the_next_player = "Player 2" if the_next_player == "Player 1" else "Player 1"
    
    selected_card = current_round[election_index - 1]

    the_middle_color, the_number_in_the_middle = the_card_in_the_middle.split()
    selected_color, selected_number = selected_card.split()

    if selected_color == the_middle_color or selected_number == the_number_in_the_middle:
        current_round.remove(selected_number)
        the_card_in_the_middle =selected_card
        print(f"\n{the_next_player}, '{selected_card}' kartını oynadı.")
        
        #if selected_color == the_middle_color and selected_number == "+2":
            


        if len(current_round) == 0:
            print("\n" + "*"*40)
            print(f"Tebrikler! {the_next_player} Tüm Kartlarını Bitirdi Ve Oyunu Kazandı!")
            print("*"*40)
            break

        the_next_player = "Player 2" if the_next_player == "Player 1" else "Player 1"

    else:
        print("\nHATA: Seçtiğiniz kart ortadaki kartla uyuşmuyor (Renk veya Sayı aynı olmalı)!")
"""
import random

# ==========================================
# 1. KART YAPISI VE DESTE OLUŞTURMA
# ==========================================
renkler = ["Kırmızı", "Mavi", "Yeşil", "Sarı"]
sayilar = [str(i) for i in range(10)]  # 0'dan 9'a kadar sayılar

deste = []
for renk in renkler:
    for sayi in sayilar:
        # Kartları "Renk Sayı" formatında metin olarak tutuyoruz. Örn: "Kırmızı 5"
        deste.append(f"{renk} {sayi}")

# Desteyi rastgele karıştırıyoruz
random.shuffle(deste)

# ==========================================
# 2. OYUNCULAR VE KART DAĞITMA
# ==========================================
# İki oyuncunun elindeki kartları ayrı listelerde tutuyoruz
# ==========================================
# 2. OYUNCULAR VE KART DAĞITMA (DİNAMİK)
# ==========================================
oyuncular = {}

# Kullanıcıdan geçerli bir oyuncu sayısı alalım (En az 2 oyuncu olmalı)
while True:
    oyuncu_sayisi_input = input("Kaç kişi oynayacak? (En az 2): ")
    if oyuncu_sayisi_input.isdigit() and int(oyuncu_sayisi_input) >= 2:
        oyuncu_sayisi = int(oyuncu_sayisi_input)
        break
    print("Geçersiz giriş! Lütfen en az 2 olacak şekilde bir sayı girin.")

# Döngüyle her oyuncunun ismini alıp sözlüğe (dict) ekliyoruz
for i in range(1, oyuncu_sayisi + 1):
    while True:
        isim = input(f"{i}. Oyuncunun ismi ne olsun?: ").strip()
        if isim and isim not in oyuncular:  # Boş isim veya aynı isim engelleniyor
            oyuncular[isim] = []
            break
        print("Geçersiz veya zaten alınmış bir isim girdiniz!")

# Her oyuncuya başlangıçta desteden 5'er kart dağıtalım
for _ in range(5):
    for oyuncu in oyuncular:
        oyuncular[oyuncu].append(deste.pop())

# Ortaya ilk kartı açıyoruz
ortadaki_kart = deste.pop()

# Oyuna ilk ismi girilen oyuncudan başlıyoruz
oyuncu_listesi = list(oyuncular.keys())
siradaki_index = 0
siradaki_oyuncu = oyuncu_listesi[siradaki_index]

# ==========================================
# 3. OYUN AKIŞI VE KURALLARI
# ==========================================
while True:
    print("\n" + "="*40)
    print(f"ORTADAKİ KART: [ {ortadaki_kart} ]")
    print(f"SIRA KİMDE: {siradaki_oyuncu}")
    print("="*40)
    
    # Sıradaki oyuncunun elini gösterelim
    mevcut_el = oyuncular[siradaki_oyuncu]
    print("Kartlarınız:")
    for i, kart in enumerate(mevcut_el, 1):
        print(f"{i}. {kart}")
    print(f"0. Pas Geç / Desteden Kart Çek")
    
    # Kullanıcıdan hamle alalım
    secim = input("\nOynamak istediğiniz kartın numarasını seçin: ")
    
    # Girdi kontrolü
    if not secim.isdigit() or int(secim) < 0 or int(secim) > len(mevcut_el):
        print("Geçersiz bir seçim yaptınız, lütfen tekrar deneyin.")
        continue
        
    secim_index = int(secim)
    
    # OYUNCU PAS GEÇERSE VEYA KART ÇEKERSE
    if secim_index == 0:
        if len(deste) > 0:
            cekilen_kart = deste.pop()
            mevcut_el.append(cekilen_kart)
            print(f"\nDesteden bir kart çektiniz: {cekilen_kart}")
        else:
            print("\nDeste bitti! Kart çekemiyorsunuz, pas geçildi.")
            
        # Sırayı diğer oyuncuya devret
        siradaki_oyuncu = "Oyuncu 2" if siradaki_oyuncu == "Oyuncu 1" else "Oyuncu 1"
        continue

    # OYUNCU KART SEÇERSE
    secilen_kart = mevcut_el[secim_index - 1]
    
    # Kartların uyum kontrolü (Renk veya Sayı eşleşmesi)
    orta_renk, orta_sayi = ortadaki_kart.split()
    secilen_renk, secilen_sayi = secilen_kart.split()
    
    if secilen_renk == orta_renk or secilen_sayi == orta_sayi:
        # Geçerli hamle: Kartı elden çıkar ve ortaya koy
        mevcut_el.remove(secilen_kart)
        ortadaki_kart = secilen_kart
        print(f"\n{siradaki_oyuncu}, '{secilen_kart}' kartını oynadı.")
        
        # OYUN SONU KONTROLÜ
        if len(mevcut_el) == 0:
            print("\n" + "*"*40)
            print(f"TEBRİKLER! {siradaki_oyuncu} TÜM KARTLARINI BİTİRDİ VE KAZANDI!")
            print("*"*40)
            break
            
        # Sırayı değiştir
        siradaki_oyuncu = "Oyuncu 2" if siradaki_oyuncu == "Oyuncu 1" else "Oyuncu 1"
    else:
        print("\nHATA: Seçtiğiniz kart ortadaki kartla uyuşmuyor (Renk veya Sayı aynı olmalı)!")