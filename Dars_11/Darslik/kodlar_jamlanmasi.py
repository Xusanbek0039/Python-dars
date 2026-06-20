# # Kod_1

# f = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "rang": "Qora"
# }
# print(f)










# # Kod_2

# f = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# print(f["model"])














# # Kod_3

# f = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964,
# "year": 2020
# }
# print(f)











# # # Kod-4
# f = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 2020,
# "year": 2025
# }
# print(len(f))










# # Kod_5
# f = {
# "brand": "Ford",
# "electric": False,
# "year": 1964,
# "colors": ["red", "white", "blue"]
# }
# print(type(f))










# # KOd_6
# f = {
# "brand": "Ford",
# "electric": False,
# "year": 1964,
# "colors": ["red", "white", "blue"]
# }
# x= f["year"]
# print(x)













# # Kod_7
# f = {
# "brand": "Ford",
# "electric": False,
# "year": 1964,
# "colors": ["red", "white", "blue"],
# "model": None
# }
# c = f.get("model")
# print(c)













# # Kod_8
# f = {
# "brand": "Ford",
# "electric": False,
# "year": 1964,
# "colors": ["red", "white", "blue"]
# }

# b = f.keys()
# print(b)











# # Kod_9
# f = {
# "brand": "Ford",
# "electric": False,
# "year": 1964,
# "colors": ["red", "white", "blue"]
# }

# v = f.values()
# print(v)














# # Kod_10
# f = {
# "brand": "Ford","electric": False,"year": 1964,"colors": ["red", "white", "blue"]
# }

# m = f.items()
# print(m)














# # Kod_11
# f = {
#     "brand": "Ford",
#     "electric": False,
#     "year": 1964,
#     "colors": ["red", "white", "blue"]
# }

# if "brand" in f:
#     print("Brand nomli kalit mavjud!")
#     # update() lug'atni eski qiymat bilan alishtirish:
# f.update({"year": 2023})
# print(f["year"])














# # Kod_12
# f = {
# "brand": "Ford",
# "model": "Mustang",
# "electric": False,
# "year": 1964,
# "colors": ["red", "white", "blue"]
# }

# f["tezlik"] = 100
# print(f)









# # Kod_13

# f = {
# "brand": "Ford",
# "electric": False,
# "year": 1964,
# "colors": ["red", "white", "blue"]
# }

# f.pop("brand")
# print(f)













# # Kod_14

# f = {
# "brand": "Ford",
# "electric": False,
# "year": 1964,
# "colors": ["red", "white", "blue"]
# }

# x=f.popitem()
# print(f)
# print(x)










# # Kod_15
# f = {
# "brand": "Ford",
# "electric": False,
# "year": 1964,
# "colors": ["red", "white", "blue"]
# }

# del f["colors"]
# print(f)











# # Kod-16
# f = {
# "brand": "Ford",
# "electric": False,
# "year": 1964,
# "colors": ["red", "white", "blue"]
# }

# f.clear() #ro’yxatni tozalash uchun ishlatilinadi:
# print(f)










# # Kod_17
# f = {
# "brand": "Ford",
# "electric": False,
# "year": 1964,
# "colors": ["red", "white", "blue"]
# }

# for l in f:
# 	print(l)








# # Kod_18/

# f = {
# "brand": "Ford",
# "electric": False,
# "year": 1964,
# "colors": ["red", "white", "blue"]
# }

# for p in f:
# 	print(f[p])












# # Kod_19
# f = {
# "brand": "Ford",
# "electric": False,
# "year": 1964,
# "colors": ["red", "white", "blue"]
# }

# for i in f.values():
#     print(i)















# # Kod_20
# f = {
# "brand": "Ford",
# "electric": False,
# "year": 1964,
# "colors": ["red", "white", "blue"]
# }

for t,e in f.items():
    if t == "colors":
        print(f"{t}")
        for rang in e:
            print(f"          -{rang}")
    else:
        print(f"{t} {e}")














# # Kod_21
# f = {
# "brand": "Ford",
# "electric": False,
# "year": 1964,
# "colors": ["red", "white", "blue"]
# }

# q = f.copy()
# print(q)


















# # Kod_22

# myfamily = {
#     "child": {
#         "name": "Xusanbek",
#         "year": 2004
#     },
#     "child2": {
#         "name": "Kamola",
#         "year": 2001
#     },
#     "child3": {
#         "name": "Fotima",
#         "year": 2004
#     }
# }














# # Kod_23

# child1 = {
#     "name": "Xusanbek",
#     "year": 2005
# }

# child2 = {
#     "name": "Kamola",
#     "year": 2002
# }

# child3 = {
#     "name": "Fotima",
#     "year": 2005
# }

# myfamily = {
#     "child1": child1,
#     "child2": child2,
#     "child3": child3
# }





