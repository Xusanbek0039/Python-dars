# # Kod_1
# car0 = {
#     'model': 'lacetti',
#     'rang': 'oq',
#     'yil': 2018,
#     'narh': 13000,
#     'km': 50000,
#     'korobka': 'avtomat'
# }

# car1 = {
#     'model': 'nexia 3',
#     'rang': 'qora',
#     'yil': 2015,
#     'narh': 9000,
#     'km': 89000,
#     'korobka': 'mexanika'
# }

# car2 = {
#     'model': 'gentra',
#     'rang': 'qizil',
#     'yil': 2019,
#     'narh': 15000,
#     'km': 20000,
#     'korobka': 'mexanika'
# }















# # Kod_2

# car0 = {
#     'model': 'lacetti',
#     'rang': 'oq',
#     'yil': 2018,
#     'narh': 13000,
#     'km': 50000,
#     'korobka': 'avtomat'
# }

# car1 = {
#     'model': 'nexia 3',
#     'rang': 'qora',
#     'yil': 2015,
#     'narh': 9000,
#     'km': 89000,
#     'korobka': 'mexanika'
# }

# car2 = {
#     'model': 'gentra',
#     'rang': 'qizil',
#     'yil': 2019,
#     'narh': 15000,
#     'km': 20000,
#     'korobka': 'mexanika'
# }


# car = car0
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")

# car = car1
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")

# car = car2
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")


















# Kod_3
# malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
# for n in range(10):
#     new_car = { # har bir yangi mashina uchun lug'at yaratamiz
#         'model':'malibu',
#         'rang':None, # rangi noaniq
#         'yil':2020,
#         'narh':None, # narhi belgilanmagan
#         'km':0,
#         'korobka':'avto'
#         }
#     malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz














# # Kod_4
# for malibu in malibus[:3]:
#     malibu['rang']='qizil'












# # Kod_5
# for malibu in malibus[3:6]:
#     malibu['rang']='qora'















# # Kod_6
# for malibu in malibus[6:]: # ohirgi 4 ta mashinani
#     malibu['rang']='qora'  # rangi qora
#     malibu['korobka']='mexanika' # korobkasi mexanika














# # Kod_7
# for malibu in malibus[6:]: # ohirgi 4 ta mashinani
#     malibu['rang']='qora'  # rangi qora
#     malibu['korobka']='mexanika' # korobkasi mexanika











# # Kod_8
# for malibu in malibus:
#     if malibu['korobka']=='avto':
#         malibu['narh']=40000
#     else:
#         malibu['narh']=35000










# 
# # Kod_9


# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']}
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())
