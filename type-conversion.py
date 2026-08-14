x = input("Birinci sayıyı giriniz: ")
y = input("İkinci sayıyı giriniz: ")
toplam = int(x) + int(y)  #eğer x ve y sayısal değerler ise, int() fonksiyonu ile string ifadeleri sayısal değerlere dönüştürürüz.
#int() değerine dönüştürülmezse, toplam içerisindeki x ve y string ifadeleri birleştirilir ve sonuç "1020" olur.
print("Toplam: ", toplam) # 30, sayısal toplama işlemi

print(type(x)) 
print(type(y))

toplam = int(x) + int(y)
print(toplam)

#ekranda str yazmasının nedeni değeri ilk önce string olaerak almasıdır. 
# input() fonksiyonu ile alınan değerler her zaman string tipindedir. 
#Bu nedenle, sayısal işlemler yapabilmek için bu değerleri int() veya --
#float() gibi uygun veri tipine dönüştürmek gerekir.

x = 5            #int
y = 2.5          #float
name = 'Elif'    #string
isOnline = True  #bool

#print(type(x))        # <class 'int'>
#print(type(y))        # <class 'float'>
#print(type(name))     # <class 'str'>       
#print(type(isOnline)) # <class 'bool'>

#Type Conversion (Tip Dönüşümü)

#int_to_float = float(x)  #int tipindeki x değişkenini float tipine dönüştürdük.
#float_to_int = int(y)    #float tipindeki y değişkenini int tipine dönüştürdük.
#int_to_str = str(x)      #int tipindeki x değişkenini string tipine dönüştürdük.
#str_to_int = int('10') 

x = float(x)
print(x)
print(type(x))  # <class 'float'>

y = int(y)
print(y)
print(type(y))  # <class 'int'>

#result = str(x) + str(y)  # x ve y değişkenlerini string tipine dönüştürdük ve birleştirdik.
#print(result)  # 5.02

result = x + y  # x ve y değişkenlerini topladık.
print(result)  # 7.5
print(type(result))  # <class 'float'>

# bool tip dönüşümü 
# bool to str
isOnline = True
isOnline_str = str(isOnline)  # bool tipindeki isOnline değişkenini string
print(isOnline)
print(type(isOnline))  # <class 'bool'>

#bool to int
isOnline = True
isOnline = int(isOnline)  # bool tipindeki isOnline değişkenini int tipine dönüştürdük.
print(isOnline)  # 1
print(type(isOnline))  # <class 'int'>