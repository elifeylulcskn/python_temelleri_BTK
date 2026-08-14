'''
    Daire Alanı : πr2
    Daire Çevresi : 2πr

    *Yarı çapı kullanıcıdan alıp dairenin alanını ve çevresini hesaplayınız. (r: 3.14) 

'''

daire_yaricap = float(input("Dairenin yarıçapını giriniz: "))
daire_alan = 3.14 * (daire_yaricap ** 2)
daire_cevre = 2 * 3.14 * daire_yaricap
print("Dairenin Alanı: ", daire_alan)
print("Dairenin Çevresi: ", daire_cevre)

# İkinci işlem -------

pi = 3.14
r = float(input("Dairenin yarıçapını giriniz: "))

alan = pi * (r ** 2)
cevre = 2 * pi * r

print("Alan", alan)
print("çevre", cevre)
