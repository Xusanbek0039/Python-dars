"""   Python polimorfizmi """
# IT_Creative uchun mahsus 
# O'tkan darslik yani class mavzusi davomiyligi, class metodi argumentlari yani funksiyasi ustida amallar davomi:

# # Kod_1
# x = "Hello World!"

# print(len(x))







# # Kod_2
# mytuple = ("apple", "banana", "cherry")      #myturple nomli kortej

# print(len(mytuple))







# # Kod_3
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(len(thisdict))






# # Kod_4
# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")   #drive=haydamoq

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")    # sail = suzmoq

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")    #fly = uchmoq

# car1 = Car("Ford", "Mustang")      #Avtomobil sinfini yaratdik
# boat1 = Boat("Ibiza", "Touring 20") #Qayiq sinfini yaratdik
# plane1 = Plane("Boeing", "747")     #Samolyot sinfini yaratdik

# for x in (car1, boat1, plane1):
#   x.move()








# # Kod_5
# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):            #Vehicle = transport 
#   pass                          #pass = o'tkazib yuborish 

# class Boat(Vehicle):
#   def move(self):                   #move = harakat
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")                    #Avtomobil sinfini yaratdik
# boat1 = Boat("Ibiza", "Touring 20")              #Qayiq sinfini yaratdik
# plane1 = Plane("Boeing", "747")                  #Samolyot sinfini yaratdik

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()






# Kod_6
# class Figure:                    #Figure = shakl
#     def area(self):               #area = hudud
#         pass                     #pass = o'tkazib yuborish
    
#     def draw(self):                 #drave = davlat
#         pass

# class Rectangle(Figure):                               #Rectangle = to'rtburchak
#     def area(self):
#         # to'rtburchakning yuzasini hisoblash

#     def draw(self):
#         # to'rtburchakni chizish

# class Circle(Figure):                               #circle = doira
#     def area(self):
#         # doira yuzasini hisoblash

#     def draw(self):                      #drawe = chizish
#         # doirani chizish

# # Barcha sinflarni bir xil usul bilan ishlatish
# def print_area_and_draw(figures):
#     for figure in figures:
#         print("Area:", figure.area())
#         figure.draw()

# # Sinflardan obyektlar yaratish
# rectangle = Rectangle()
# circle = Circle()

# # print_area_and_draw funktsiyasini sinflar ro'yxati bilan chaqirish
# print_area_and_draw([rectangle, circle])
