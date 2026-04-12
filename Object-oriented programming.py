#1st Questions
class Urun:
    def __init__ (self,isim,stok,fiyat):
        self.isim=isim
        self.stok=stok
        self.fiyat=fiyat
    def stok_guncelle(self,yeni_stok):
        self.stok=yeni_stok
class Sepet:
    def __init__(self):
        self.urunler=[]
    def urun_ekle(self,urun):
        self.urunler.append(urun)
    def urun_cikar(self,urun):
        self.urunler.remove(urun)
    def toplam_fiyat(self):
        toplam=0
        for urun in self.urunler:
            toplam+=urun.fiyat
        return toplam

#2nd Questions
class BankaHesabi:
    def __init__(self,isim,bakiye):
        self.isim=isim
        self.bakiye=bakiye
        self.history=[]
    def para_yatir(self,miktar):
        self.bakiye+=miktar
        self.history.append(self.para_yatir)
    def para_cek(self,miktar):
        if miktar>self.bakiye:
            print("Yetersiz Bakiye!!")
        else:
            self.bakiye-=miktar
            self.history.append(self.para_cek)
    def gecmis(self):
        print(self.history)

#3rd Questions
class Book:
    def __init__(self,isim,yazar,durum):
        self.isim=isim
        self.yazar=yazar
        self.durum=durum
    def book_info(self):
        return f"Kitap: {self.isim}, Yazar: {self.yazar}, Durum: {self.durum}"
class User:
    def __init__(self,isim,aldigi_kitaplar):
        self.isim=isim
        self.aldigi_kitaplar=aldigi_kitaplar
class Library:
    def __init__(self):
        self.books=[]
    def book_add(self,Book):
        self.books.append(Book)
    def book_remove(self,Book):
        self.books.remove(Book)
    def book_list(self):
        for Book in self.books:
            print(Book.book_info())

#4th Questions
class Car:
    def __init__(self,marka,gunluk_fiyat,musait_mi):
        self.marka=marka
        self.gunluk_fiyat=gunluk_fiyat
        self.musait_mi=musait_mi
    def car_info(self):
        return f"Araba: {self.marka}, Günlük Fiyatı: {self.gunluk_fiyat}, Durumu: {self.musait_mi}"
class User1:
    def __init__(self,isim):
        self.isim=isim
        self.cars=[]
    def car_add(self,Car):
        self.cars.append(Car)
    def car_list(self):
        for Car in self.cars:
            print(Car.car_info())

#5th Questions
class Mission:
    def __init__(self,baslik,aciklama,tamamlandi_mi):
        self.baslik=baslik
        self.aciklama=aciklama
        self.tamamlandi_mi=tamamlandi_mi
    def mission_info(self):
        return f"Görev: {self.baslik}, Açıklama: {self.aciklama}, Durumu: {self.tamamlandi_mi}"
class User2:
    def __init__(self,isim):
        self.isim=isim
        self.missions=[]
    def mission_add(self,Mission):
        self.missions.append(Mission)
    def mission_remove(self,Mission):
        self.missions.remove(Mission)
    def mission_list(self):
        for Mission in self.missions:
            print(Mission.mission.info())