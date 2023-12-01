# Kod_1
# def toliq_ism_yasa(ism, familiya):
#     """Toliq isma qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz
# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")









# Kod_2
# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
# talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")







# # KOd_3
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")







# KOd_4
# def oraliq(min,max):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar

# print(oraliq(0,10))
# print(oraliq(10,21))









# # KOd_5

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi):
#     avto = {
#         'kompaniya': kompaniya,
#         'model': model,
#         'rangi': rangi,
#         'korobka': korobka,
#         'yili': yili,
#         'narhi': narhi
#     }
#     return avto

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar = []  # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narhi = input("Narhi: ")

#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))

#     javob = input("Yana aftomobil qo'shasizmi? (yes/no): ")
#     if javob == 'no':
#         break

# # Avtolar ro'yxatini chiqarish
# for avto in avtolar:
#     print(f"Kompaniya nomi: {avto['kompaniya']}"
#           f"Mashina modeli: {avto['model']}"
#           f"Mashina rangi: {avto['rangi']}"
#           f"Mashina yuritgichi: {avto['korobka']}"
#           f"Mashina ishlab chiqarilgan yili: {avto['yili']}"
#           f"Mashina narxi:{avti['narhi']}$")











# Kod_6
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(f"Alining baxosi: {baholar['ali']}\n"
#       f"Valining baxosi: {baholar['vali']}\n"
#       f"Hasanning baxosi: {baholar['hasan']}\n"
#       f"Husanning baxosi: {baholar['husan']}")













# Kod_7
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(talabalar)









# Kod_8
def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar[:])
print(talabalar)

