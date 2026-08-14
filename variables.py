brut_maas = int(input("Brüt maaşınızı giriniz: "))
brut_maas = brut_maas - brut_maas * 0.27
print("Brüt maaşınız: ", brut_maas)
brut_maas2 = int(input("2. kullanıcı, Brüt maaşınızı giriniz: ")) #4000 maas
brut_maas2 = brut_maas2 - brut_maas2 * 0.27
print("2. kullanıcı, Brüt maaşınız: ", brut_maas2)

maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print( "Ali'nin net maaşı: ", maasAli - maasAli * vergi)
print( "Ahmet'in net maaşı: ", maasAhmet - maasAhmet * vergi)

     #--- Değişken Tanımlama Kuralları ---
     #Rakam ile başlayamaz.
number1 = 10
print(number1)
number1 = 20
print(number1)

     #Aynı isimle iki değişken tanımlanamaz.
     #Değişken isimleri büyük harfle başlayamaz.
age = 20
Age = 30
print(age)
print(Age)

     #Değişken isimleri özel karakter içeremez.
_age = 20
yas = 30       #yaş olmaz
x = 10         #int
y = 2.5        #float
name = "Ali"   #string
isStudent = True #bool -- true/false 

# x, y, name, isStudent = (10, 2.5, "Ali", True) -- değer ataması işle tek bir satırda yapılır.
# Soldan sağa doğru değerler atanır.

a = "10"
b = "20"
print(a+b) #30 - 1020, string birleştirme işlemi yapar.

first_name = "Ali"
last_name = " Veli"
print(first_name + " " + last_name) #Ali Veli





