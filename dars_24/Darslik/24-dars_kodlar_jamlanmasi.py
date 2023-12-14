"""Python doirasi"""

"""24-dars kodlar jamlanmasi"""
# Kod 1

# def myfunc():
  
#   x = 300
#   print(x)

# myfunc()







# # Kod_2
# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()

# myfunc()






# # Kod_3
# x = 300

# def myfunc():
#   print(x)

# myfunc()

# print(x)




# # Kod_4
# x = 300

# def myfunc():
#   x = 200
#   print(x)

# myfunc()

# print(x)





# # Kod_5
# def myfunc():
#   global x
#   x = 300

# myfunc()

# print(x)








# # Kod_6
# x = 10

# def func():
#     global x
#     x = 20
#     print(x)

# func()
# print(x)








# Kod_7
# x = 300

# def myfunc():
#   global x
#   x = 200

# myfunc()

# print(x)








x = 10  # O'zgaruvchiga 10 qiymatini beramiz

def update_variable():
    x = 20  # Lokal o'zgaruvchini yaratamiz va qiymatini beramiz
    print("Funksiya ichida x:", x)

update_variable()  # Funktsiyani chaqiramiz

print("Tashqi qismida x:", x)
