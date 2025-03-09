# kod_1

# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q) ")
#     javob = javob.lower()
#     javob = javob.strip()
#     if javob =='ha':
#         n=1+n
#         continue
#     elif javob == "yo'q":
#         break
#     else:
#         print("Iltimos to'g'ri matindan foydalaning ha/yo'q: ")


# print("Do'stlaringiz ro'yxati: ")
# for ism in ismlar:
#     print(ism.title())




















# kod_2


# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)\t")
#     javob = javob.lower()
#     javob = javob.strip()
#     if javob == "yo'q":
#         ishora = False
#     elif javob == "ha":
#         continue


# for ism, yosh in dostlar.items():
#     print(f"\n{ism.title()} {yosh} yoshda!")





















# kod_3
# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
#     cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
# print(cars)

















# kod_4

# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho
# print(baholangan_talabalar)
