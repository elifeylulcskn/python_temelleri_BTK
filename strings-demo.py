website = "http://www.sadikturan.com"
course = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama Kursu (40 Saat)"

# 1 - 'course' karakter dizisinin uzunluğunu hesaplayınız.
result = len(course)
print("Course Length:", result)

#2 - 'website' içinden www karakterini alın.
www_index = website.find("www")
print("Index of 'www':", www_index)

# 3 - 'website' içinden com karakterini alın.
com_index = website.find("com")
print("Index of 'com':", com_index)

# 4 - 'course' içinden ilk 15 ve son 15 karakteri alın.
first_15_chars = course[:15]
last_15_chars = course[-15:]
print("First 15 characters of course:", first_15_chars)
print("Last 15 characters of course:", last_15_chars)

# 5 - 'course' ifadesindeki karakterleri tersten yazdırınız.
reversed_course = course[::-1]
print("Reversed course:", reversed_course)

name, surname, age, job = "Ali", "Veli", 32, "Mühendis"
# 6 - Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yaz
# '''Benim adım Ali Veli, Yaşım 32 ve mesleğim Mühendis.'
print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.")

# 7 - 'Hello world' ifadesindeki w harfini W ile değiştirin.
hello_world = "Hello world"
modified_hello_world = hello_world.replace("w", "W")
print("Modified Hello World:", modified_hello_world)

# 8 - 'abc' ifadesini yan yana 3 defa yazdırın.
abc_repeated = "abc" * 3
print("Repeated 'abc':", abc_repeated)
