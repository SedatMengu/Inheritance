# tanımı : oluşturulan ana class dan daha düşük alt klaslar oluşturacağız. oluşturulan alt classların üst class dan aldıklarına inheritance denecek.

# çalışanlar : isim , soyisim , email , maaş
# yazılımcı ; müdür
# backend , frontend ; Arge müdürü , Ürün müdür , genel müdür

# 3 farklı senaryo olarka inceleyeceğiz.
# senaryo1 : ana iskeletle birebir aynı olan bir alt sınıf

class calisan:                                                                                                                                        # / iskelet bir class oluşturduk. daha sonra buraya herhangi bir fonksiyon vs ekleyebiliriz.
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim=soyisim
        self.maas=maas
        self.email = isim + soyisim + "@sirket.com"                      # / dışardan almadığımız için __init__ kısmına yazmaya gerek duymadık.
    def bilgileri_goster(self):
         return "isim: {}  , soyisim : {}  , maas : {}  , email : {} ".format(self.isim,self.soyisim,self.maas,self.email)

calisan1 = calisan("sedat","mengu",6000)                                 # / çalışan1 diye nesne türettik.
calisan2 = calisan("adnan","lüle",7000)                                  # / çalışan2 diye nesne türettik.

print(calisan1.bilgileri_goster())                                       # / isim: sedat  , soyisim : mengu  , maas : 6000  , email : sedatmengu@sirket.com
print(calisan2.bilgileri_goster())                                       # / isim: adnan  , soyisim : lüle  , maas : 7000  , email : adnanlüle@sirket.com

class yazilimci(calisan):                                                                                                                    
    pass
yazilimci1=yazilimci("osman","pazar",7000)                               
yazilimci2=yazilimci("emre","omurgalı",12000)

print(yazilimci1.bilgileri_goster())                                     # / isim: osman  , soyisim : pazar  , maas : 7000  , email : osmanpazar@sirket.com          # türetilen class içerisinde bilgileri_goster fonksiyonu olmadığı için main class dan aldı.
print(yazilimci2.bilgileri_goster())                                     # / isim: emre  , soyisim : omurgalı  , maas : 12000  , email : emreomurgalı@sirket.com     # türetilen class içerisinde bilgileri_goster fonksiyonu olmadığı için main class dan aldı.


# eğer aynı tanımlama (verilen örnek zam oranı) türetilen sınıf içerisinde ayrıca tanımlanmadıysa ana iskeletten çeker , tanımlı ise ana iskeleti ezer.

class calisan:
    zam_orani=1.1                                                                                                                              
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim=soyisim
        self.maas=maas
        self.email = isim + soyisim + "@sirket.com"  

calisan1 = calisan("sedat","mengu",6000) 
calisan2=calisan("adnan","lüle",7000)  

class yazilimci(calisan):                                                                                                                      
    zam_orani=1.2
yazilimci1=yazilimci("osman","pazar",7000)                                                                              
yazilimci2=yazilimci("emre","omurgalı",12000)

print(calisan1.zam_orani)                                                  # /  1.1  / main class dan aldı
print(yazilimci1.zam_orani)                                                # /  1.2  / yazılımcı için tanımlanan class dan aldı. eğer türetilen class da olmasaydı main class dan alacaktı (1.1)

# aynı isimde bile olsa türetilen class da bulunan fonksiyon main class ı ezer.

class calisan:                                                                                                                                        # / iskelet bir class oluşturduk. daha sonra buraya herhangi bir fonksiyon vs ekleyebiliriz.
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim=soyisim
        self.maas=maas
        self.email = isim + soyisim + "@sirket.com"                      # / dışardan almadığımız için __init__ kısmına yazmaya gerek duymadık.
    def bilgileri_goster(self):
         return "isim: {}  , soyisim : {}  , maas : {}  , email : {} ".format(self.isim,self.soyisim,self.maas,self.email)

calisan1 = calisan("sedat","mengu",6000)                                 # / çalışan1 diye nesne türettik.
calisan2 = calisan("adnan","lüle",7000)                                  # / çalışan2 diye nesne türettik.

print(calisan1.bilgileri_goster())                                       # / isim: sedat  , soyisim : mengu  , maas : 6000  , email : sedatmengu@sirket.com
print(calisan2.bilgileri_goster())                                       # / isim: adnan  , soyisim : lüle  , maas : 7000  , email : adnanlüle@sirket.com

class yazilimci(calisan):                                                                                                                    
    def bilgileri_goster(self):
        return "yazılım classı içindeki bilgileri göster fonksiyonu çalışıyor"

yazilimci1=yazilimci("osman","pazar",7000)                               
yazilimci2=yazilimci("emre","omurgalı",12000)

print(yazilimci1.bilgileri_goster())                                     # / "yazılım classı içindeki bilgileri göster fonksiyonu çalışıyor"
print(yazilimci2.bilgileri_goster())                                     # / "yazılım classı içindeki bilgileri göster fonksiyonu çalışıyor"


#  türetilen class a init ile özellik ekleme : 

class calisan:                                                                                                                                        
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim=soyisim
        self.maas=maas
        self.email = isim + soyisim + "@sirket.com"
    def bilgileri_goster(self):
         return "isim: {}  , soyisim : {}  , maas : {}  , email : {}".format(self.isim,self.soyisim,self.maas,self.email)

calisan12 = calisan("Ender","Uslu",9000)
calisan13 = calisan("utku","sarı",8000)

class yazilimci(calisan):                                                                                                                       
    def __init__(self, isim, soyisim, maas,bildigi_dil):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email =  isim + soyisim + "@sirket.com"
        self.bildigi_dil = bildigi_dil
    def bilgileri_goster(self):
         return "isim: {}  , soyisim : {}  , maas : {}  , email : {} , Bildiği dil:  {} ".format(self.isim,self.soyisim,self.maas,self.email,self.bildigi_dil)
    
yazilimci21 = yazilimci("cem","duran",6000,"python")
yazilimci22 = yazilimci("latif","gür",9000,"c#")

print(yazilimci21.bilgileri_goster())           # / isim: cem  , soyisim : duran  , maas : 6000  , email : cemduran@sirket.com , Bildiği dil:  python
print(yazilimci22.bilgileri_goster())           # / isim: latif  , soyisim : gür  , maas : 9000  , email : latifgür@sirket.com , Bildiği dil:  c# 
print(calisan12.bilgileri_goster())             # / isim: Ender  , soyisim : Uslu  , maas : 9000  , email : EnderUslu@sirket.com
print(calisan13.bilgileri_goster())             # / isim: utku  , soyisim : sarı  , maas : 8000  , email : utkusarı@sirket.com

# bilgileri_goster fonksiyonu hangi class dan türetilen bir nesne ise o class da tanımlı olan hali ile yazdırılır.

# super().__init__ kavramı

# türetilen class da tekrar tekrar self.isim=isim self.soyisim=soyisim yazmaktansa super() __init__ kullanılabilir.

class calisan:                                                                                                                                        
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim=soyisim
        self.maas=maas
        self.email = isim + soyisim + "@sirket.com"
    def bilgileri_goster(self):
         return "isim: {}  , soyisim : {}  , maas : {}  , email : {}".format(self.isim,self.soyisim,self.maas,self.email)

calisan12 = calisan("Ender","Uslu",9000)
calisan13 = calisan("utku","sarı",8000)

class yazilimci(calisan):                                                                                                                       
    def __init__(self, isim, soyisim, maas,bildigi_dil):
        super().__init__(isim,soyisim,maas) 
        self.bildigi_dil = bildigi_dil
    def bilgileri_goster(self):
         return "isim: {}  , soyisim : {}  , maas : {}  , email : {} , Bildiği dil:  {} ".format(self.isim,self.soyisim,self.maas,self.email,self.bildigi_dil)
    
yazilimci21 = yazilimci("cem","duran",6000,"python")
yazilimci22 = yazilimci("latif","gür",9000,"c#")

print(yazilimci21.bilgileri_goster())           # / super().__init__ ekledik çıktı değişmedi . yukarısı ile aynı isim: cem  , soyisim : duran  , maas : 6000  , email : cemduran@sirket.com , Bildiği dil:  python
print(yazilimci22.bilgileri_goster())           # / super().__init__ ekledik çıktı değişmedi . yukarısı ile aynı isim: latif  , soyisim : gür  , maas : 9000  , email : latifgür@sirket.com , Bildiği dil:  c# 
print(calisan12.bilgileri_goster())             # / super().__init__ ekledik çıktı değişmedi . yukarısı ile aynı isim: Ender  , soyisim : Uslu  , maas : 9000  , email : EnderUslu@sirket.com
print(calisan13.bilgileri_goster())             # / super().__init__ ekledik çıktı değişmedi . yukarısı ile aynı isim: utku  , soyisim : sarı  , maas : 8000  , email : utkusarı@sirket.com


# yönetici oluşturup , çalışan ekleme , çalışan silme , sorumlu olduğu çalışanları listeleme operasyonları

class calisan:                                                                                                                                        # / iskelet bir class oluşturduk. daha sonra buraya herhangi bir fonksiyon vs ekleyebiliriz.
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim=soyisim
        self.maas=maas
        self.email = isim + soyisim + "@sirket.com"                      # / dışardan almadığımız için __init__ kısmına yazmaya gerek duymadık.
    def bilgileri_goster(self):
        return ("isim: {}  , soyisim : {}  , maas : {}  , email : {} ".format(self.isim,self.soyisim,self.maas,self.email))
    

calisan1 = calisan("sedat","mengu",6000)                                 
calisan2 = calisan("adnan","lüle",7000)                                  

class yonetici(calisan):                                        # / calisan classından yönetici class ı tanımladık
    def __init__(self, isim, soyisim, maas,calisanlar=None):    # / yönetici class ının kullanacağı parametreleri yazdık ve calisanları ilk etapta none olarak default ettik.
        super().__init__(isim, soyisim, maas)                   # / super fonksiyonu ile inheritance ettik.
        if calisanlar == None:                                  # / eğer calışanlar None ise boş bir dizi oluşturduk
            self.calisanlar=[]
        else:
            self.calisanlar = calisanlar                        # eğer none değil ise klasik self tanımlamamızı yaptık.

    def calisan_ekle(self,calisan):                             # çalışan eklemek için bir fonksiyon yazıyoruz,
        if calisan not in self.calisanlar:                      # eğer eklenmek istenen çalışan self.çalışanlar listesinde var değil ise
            self.calisanlar.append(calisan)                     # append ile listenin sonuna ekle
        
    def calisan_sil(self,calisan):                              # çalışan silmek için bir fonksiyon yazıyoruz,
        if calisan in self.calisanlar:                          # eğer silmek istediğimiz çalışan self.çalışanlar listesinde var ise 
            self.calisanlar.remove(calisan)                     # çalılanı remove et

    def calisanlari_goster(self):                              # çalışanları listelemek için bir fonksiyon yazıyoruz
        for calisan in self.calisanlar:                         # liste yazdırmak için klasik olduğu üzere for döngüsünden faydalanacağız
            print(calisan.bilgileri_goster())                    # self.calisanlar dizisindeki bütün elemanları calisan indexine eşitle ve print ile ekrana bastır dedik.


yonetici100 = yonetici("Ahmet","Kale",17000)                 # / yönetici oluşturduk.

yonetici100.calisan_ekle(calisan1)                                # daha önce tanımladığımız çalışan1 i ekledik
yonetici100.calisan_ekle(calisan2)                                # daha önce tanımladığımız çalışan2 i ekledik

yonetici100.calisanlari_goster()
print("**************************")
yonetici100.calisan_sil(calisan2)
yonetici100.calisanlari_goster()

# / yöneticide calisanlar= None olmasaydı yönetici oluştururken liste tipinde çalışanları kendimiz elle girmemiz gerekirdi.

# yonetici200 = yonetici("ahmet","olcay",12000,[calisan1,calisan2,yazilimci21])

#isinstance kullanımı : 

print(isinstance(yonetici100,calisan))       # / true döndü. sebebi ise yönetici100 nesnesi calisan sınıfından türetilmiş olmasıdır.    nesne class kontrolü
print(isinstance(calisan13,yonetici))        # / false döndü. sebebi ise calisan13 nesnesi yönetici sınıfından türetilmemiş olmasıdır.  nesne class kontrolü
print(issubclass(yonetici,calisan))          # / true döndü. sebebi ise yönetici class ı calisan classından türetilmiş olmasıdır. alt sınıf üst sınıf kontrolü