
# Kod_1
# List quyidagicha yaratiladi:
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]  # mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000]  # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5]  # sonlar va matnlar aralash ro'yxat
# ismlar = []  # bo'sh ro'yxat













# Kod_2
# LIST ELEMENTLARI
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print("Birinchi meva: ", mevalar[0])
# print("Ikkinchi meva: ", mevalar[1])









# Kod_3
# Listga string metodlarini qo’llash
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print("Birinchi meva: ", mevalar[0].title())
# print("Ikkinchi meva: ", mevalar[1].upper())









# Kod_4
# Listda arifmetik amallar bajarish:
# narhlar = [12000, 18000, 10900, 22000]
# print(narhlar[2] + narhlar[3])












# Kod_5
# Index orqali suzish
# car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
# print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz












# Kod_6
# # ELEMENTLARNI QO'SHISH, O'CHIRISH VA O'ZGARTIRISH
# narhlar = [12000, 18000, 10900, 22000]
# narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
# narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
# narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
# print(narhlar)















# Kod_7
# .append metodi
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
# print(mevalar) 











# Kod_8
# cars = [] # bo'sh ro'yxat yaratamiz
# cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
# cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
# cars.append('Cobalt') # ro'yxatga Cobalt mashinasini qo'shamiz
# print(cars)












# # Kod_9
# # .insert() metodi
# cars = ['Lacetti', 'Nexia 3', 'Cobalt']
# cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
# print(cars)A
# cars.insert(2, 'Damas') # 3-o'ringa yangi qiymat qo'shamiz
# print(cars)
















# # Kod_10
# # Elementni o'chirish
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
# print(mevalar)













# Kod_11
# # .remove() metodi 
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
# print(mevalar)











# # Kod_12
# # .remove() metodi
# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
# hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
# print(hayvonlar)














# # Kod_13
# # Elementni sug'urib olish
# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)