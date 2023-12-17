"""24-dars-kodlar-jamlanmasi """
# pip install datetime
# date time ustida amallar 
# json tushunchasi




# # Kod_1
# import datetime

# x = datetime.datetime.now()
# print(x)









# # Kod_2
# import datetime                       #import = kochirib kelish      datetime = sana vaqt 

# x = datetime.datetime.now()              #now = hozir 

# print(x.year)                            # year = yil
# print(x.strftime("%A"))       #strftime = datetime moduli funksyasi









# # Kod_3
# import datetime

# x = datetime.datetime(2020, 5, 17)

# print(x)







# # Kod_4
# import datetime

# x = datetime.datetime(2018, 6, 1)

# print(x.strftime("%x"))







# # Kod_5
# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print(x)
# print(y)







# # Kod_6
# x = abs(-7.25)     # x ga manfiy qiymat berilgan hamda abs metodi yordamida musbat songa o'girib oldik

# print(x)





# # Kod_7
# x = pow(4, 3)

# print(x)








# Kod_8
# {
#   "name": "Husan",
#   "age": 18,
#   "city": "Uzbekiston",
#   "hobbies": ["reading","photography","Full-Stack Backend Developer","network admin"],
#   "isStudent": True
# }






# Kod_9

# import json

# # JSON ma'lumotlari
# json_data = '{"name": "Xusan", "age": 18, "city": "Djizzax"}'

# # JSON dan Pythonga o'qish
# data = json.loads(json_data)           #loads = yuklash

# # Ma'lumotlarni pythonda ishlatish
# print(data["name"])  # Xusan
# print(data["age"])  # 18
# print(data["city"])  # Djizzax








# Kod_10
# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)





# # Kod_11
# import json

# print(json.dumps({"name": "Husan", "age": 18}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("Assalom alekum"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))





# # taxlil uchun kod
# import json

# x = {
#   "name": "Husan",
#   "age": 18,
#   "married": False,                            #married = uylangan(turmushga chiqgan)
#   "divorced": False,                           #divorced = ajrashgan yoki yoq
#   "children": False,                 #children = bolalari
#   "pets": None,                        #pets = uy hayvonlar
#   "cars": [
#     {"model": "BMW 230"},
#     {"model": "Ford Edge"}
#   ]
# }

# print(json.dumps(x))















