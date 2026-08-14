"""
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

    Müşteri adı
    Müşteri soyadı
    müşteri ad soyad
    müşteri cinsiyet
    müşteri tc kimlik
    müşteri doğum yılı
    müşteri adres bilgisi
    müşteri yaşı
    müşteri telefon numarası


"""
"""
    2- Siparişlerin toplam bilgisini hesaplayınız.
    Sipariş 1 => 110 TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 356.95 TL 


"""

musteri_adi = "Ali"
musteri_soyadi = "Veli"
musteri_cinsiyet = "Erkek"   #bool da olabilir , true/false şeklinde. Erkek = True, Kadın = False gibi.
musteri_tc_kimlik = "12345647353"
musteri_dogum_yili = 1999
musteri_adres_bilgisi = "İstanbul, Türkiye"
musteri_yasi = 2024 - musteri_dogum_yili
musteri_telefon_numarasi = "555-123-4567"

siparis1 = 110
siparis2 = 1100.5
siparis3 = 356.95
toplam_siparis = siparis1 + siparis2 + siparis3

print("Müşteri Adı:", musteri_adi)
print("Müşteri Soyadı:", musteri_soyadi)
print("Müşteri Cinsiyet:", musteri_cinsiyet)
print("Müşteri TC Kimlik:", musteri_tc_kimlik)
print("Müşteri Doğum Yılı:", musteri_dogum_yili)
print("Müşteri Adres Bilgisi:", musteri_adres_bilgisi)
print("Müşteri Yaşı:", musteri_yasi)
print("Müşteri Telefon Numarası:", musteri_telefon_numarasi)
print("Toplam Sipariş Tutarı:", toplam_siparis, "TL")          
