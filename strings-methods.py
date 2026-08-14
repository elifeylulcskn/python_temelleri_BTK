message =  'Hello, World! My name is Elif Eylül.'

# message message.upper() #Bütün harfleri büyük yapar.
# message = message.lower() #Bütün harfleri küçük yapar.
# message = message.title() #Her kelimenin ilk harfini büyük yapar.
# message = message.capitalize() #Sadece ilk harfi büyük yapar.

# message = message.strip() #Başındaki ve sonundaki boşlukları siler. Önemli!!!!
# message = message.lstrip() #Sadece başındaki boşlukları siler.
# message = message.rstrip() #Sadece sonundaki boşlukları siler.

message = message.split('.') #Boşluklardan ayırır ve listeye çevirir.
message = '---'.join(message) #Listeyi tekrar stringe çevirir ve araya istediğimiz karakteri koyar.

# index = message.find('Elif') #İçinde aradığımız kelimeyi bulursa indexini verir, bulamazsa -1 verir.
isFound = message.startswith('H') #İçinde aradığımız kelimeyle başlıyorsa True, başlamıyorsa False verir.
isFound = message.endswith('f') #İçinde aradığımız kelimeyle bitiyorsa True, bitmiyorsa False verir.

# message = message.replace('Elif', 'Will') #İçinde aradığımız kelimeyi bulursa onu değiştirir.
# message = message.replace('i', 'i').replace('u', 'u') #İçinde aradığımız kelimeyi bulursa onu değiştirir.

message = message.center(50, '-') #Mesajı ortalar ve başına ve sonuna istediğimiz karakteri ekler.
print(isFound)

# print(message[2])
