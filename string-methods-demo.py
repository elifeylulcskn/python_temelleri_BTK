website = "http://www.elifeylul.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberi (40 Saat)"

# 1 - 'Hello World' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
message = ' Hello World '
message = message.strip()

# 2 - 'www.elifeylul.com' içindeki elif bilgisi haricindeki her karakteri silin.
website = website[index+4:]  # 'elif' karakter dizisinin sonrasındaki kısmı alır

# 3 - 'course' içindeki tüm karakterleri küçük harf yapın.
course = course.lower()

# 4 - 'website' içinde kaç tane 'w' karakteri vardır? (count metodu ile)
w_count = website.count('w')

# 5 - 'website' 'www' ile başlayıp com ile bitiyor mu?
starts_with_www = website.startswith('www')
ends_with_com = website.endswith('com')

# 6 - 'course' içindeki tüm karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
is_alpha = course.isalpha()

# 7 - 'contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyin.
contents = 'contents'
contents_centered = contents.center(50, '*')

# 8 - 'course' içindeki tüm boşluk karakterlerini '-' ile değiştirin.
course_replaced = course.replace(' ', '-')

# 9 - 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.
message = message.replace('World', 'There')

# 10 - 'course' karakter dizisinin boşluk karakterlerinden ayırın.
#YAPILAMADI.
 