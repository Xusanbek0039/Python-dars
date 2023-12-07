# Kod_1
# class Person:
#   """Ota- ona merosini yaratamiz"""
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# #Obyekt yaratish uchun Person sinfidan foydalandik va keyin print  usulini ishlatdik:

# x = Person("Abror", "Jamolov")
# x.printname()












# Kod_2
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.sinf = 1
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya} {self.tyil}-was born in. Kimyo International University In Tashkent {self.sinf}-stage student "
# talaba1 = Talaba("Xusanbek","Suyunov",2005)
# print(talaba1.get_info())











# Kod_3
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.sinf = 1
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya} {self.tyil}-was born in. Kimyo International University In Tashkent {self.sinf}-stage student "
# talaba1 = Talaba("Xusanbek","Suyunov",2005)
# talaba1.sinf= 2
# print(talaba1.bosqich)











# Kod_4
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.sinf = 1
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya} {self.tyil}-was born in. Kimyo International University In Tashkent {self.sinf}-stage student "
#     def set_bosqich(self,sinf):
#         """Talabaning kursini yangilovchi metod"""
#         self.sinf = 2
# talaba1 = Talaba("Xusanbek","Suyunov",2005)
# talaba1.sinf= 2
# print(talaba1.get_info())







# Kod_5
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.sinf = 1
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya} {self.tyil} yilda tug'ilgan. Hozirda  Kimyo International University Toshkent shahrida {self.sinf}-bosqich talabasi"

#     def update_sinf(self, yangi_sinf):
#         """Talabaning sinfini yangilash"""
#         self.sinf = yangi_sinf

# talaba1 = Talaba("Xusanbek", "Suyunov", 2005)
# print(talaba1.get_info())
# talaba1.update_sinf(2)  # Sinfini 2-bosqichga oshiramiz
# print(talaba1.get_info())










# Kod_6
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.sinf = 1
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya} {self.tyil}-was born in. Kimyo International University In Tashkent {self.sinf}-stage student "

# class YangiTalaba(Talaba):
#     """YangiTalaba nomli yangi klass"""
#     def __init__(self, ism, familiya, tyil):
#         """YangiTalabaning xususiyatlari"""
#         super().__init__(ism, familiya, tyil)    #super funksiyasi quyidagicha ishlatilinadi
    
#     def update_sinf(self, yangi_sinf):
#         """Talabaning sinfini yangilash"""
#         self.sinf = yangi_sinf

# talaba1 = YangiTalaba("Xusanbek", "Suyunov", 2005)
# print(talaba1.get_info())
# talaba1.update_sinf(2)  # Sinfini 2-bosqichga oshiramiz
# print(talaba1.get_info())







# Kod_7
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.sinf = 1
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya} {self.tyil}-accepted. Kimyo International University In Tashkent {self.sinf}-stage student "
    
#     def graduation_year(self, years):
#         """Talabaning bitirish yilini hisoblash"""
#         return self.tyil + years

# talaba1 = Talaba("Xusanbek", "Suyunov", 2022)
# print(talaba1.get_info())
# print(f"The student will graduate in {talaba1.graduation_year(4)}")  # Bitirish yilini hisoblash
# print(f"The student will graduate with a master's degree in  {talaba1.graduation_year(4)}") #Magistraturani hisoblaymiz






# Kod_8
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.sinf = 1
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya} {self.tyil}-was born in. Kimyo International University In Tashkent {self.sinf}-stage student "

# class Fan:
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self, talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1

# talaba1 = Talaba("Xusanbek", "Suyunov", 2005)
# print(talaba1.get_info())

# fan1 = Fan("Kimyo")
# fan1.add_student(talaba1)
# print(fan1.talabalar_soni)  # Talabalar soni





# Kod_9
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.sinf = 1
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya} {self.tyil}-was born in. Kimyo International University In Tashkent {self.sinf}-stage student "

# class Fan:
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self, talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1

# talaba1 = Talaba("Juratbek", "Xazratov", 2007)
# talaba2 = Talaba("Mirjalol", "O'ktamov", 2001)
# talaba3 = Talaba("Elyorjon", "Mamatqulov", 2001)

# matematika = Fan("Oliy Matematika")
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# print(matematika.talabalar_soni)  # Talabalar soni





# Kod_10
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.sinf = 1
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya} {self.tyil}-was born in. Kimyo International University In Tashkent {self.sinf}-stage student "

# class Fan:
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self, talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
    
#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]

# talaba1 = Talaba("Alijon", "Valiyev", 2000)
# talaba2 = Talaba("Hasan", "Alimov", 2001)
# talaba3 = Talaba("Akrom", "Boriyev", 2001)

# matematika = Fan("Oliy Matematika")
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# print(matematika.get_students())  # Talabalar ro'yxati




# Kod_11
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Salom", self.firstname, self.lastname, "ning ", self.graduationyear,"-yildagi sinfiga xush kelibsiz!")

# x = Student("Xusan", "Suyunov", 2023)
# x.welcome()





# Kod_12
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
      
#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
        
#     def update_bosqich(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.bosqich += 1    
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
    
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
    
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
    
#     def get_age(self, yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil - self.tyil

# # Testing the Talaba class
# talaba1 = Talaba("Alijon", "Valiyev", 2000)
# talaba2 = Talaba("Hasan", "Alimov", 2001)
# talaba3 = Talaba("Akrom", "Boriyev", 2001)

# print(talaba1.get_info())  # Talaba haqida ma'lumot
# print(talaba2.get_name())  # Talabaning ismi
# print(talaba3.get_lastname())  # Talabaning familiyasi
# print(talaba1.get_fullname())  # Talabaning ism-familiyasi
# print(talaba2.get_age(2023))  # Talabaning yoshi










# Kod_13
# class Fan:
#     """Fan nomli klass"""
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self, talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
    
#     def get_name(self):
#         """Fan nomi"""
#         return self.nomi
    
#     def get_students(self):
#         """Fanga yozilgan talabalar haqida ma'lumot"""
#         return [x.get_info() for x in self.talabalar]
    
#     def get_students_num(self):
#         """Fanga yozilgan talabalar soni"""
#         return self.talabalar_soni


# matematika = Fan("Oliy Matematika")

# print(matematika.get_name())  # Fan nomi

# talaba1 = Talaba("Alijon", "Valiyev", 2000)
# talaba2 = Talaba("Hasan", "Alimov", 2001)
# talaba3 = Talaba("Akrom", "Boriyev", 2001)

# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# print(matematika.get_students())  # Talabalar ro'yxati
# print(matematika.get_students_num())  # Talabalar soni




# Kod_14
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.sinf = 1
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya} {self.tyil}-was born in. Kimyo International University In Tashkent {self.sinf}-stage student "
# print(dir(Talaba))



# Kod_15
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.sinf = 1
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya} {self.tyil}-was born in. Kimyo International University In Tashkent {self.sinf}-stage student "
    
#     def see_methods(self):
#         return [method for method in dir(self) if method.startswith('__') is False]


# talaba1 = Talaba("Xusanbek", "Suyunov", 2005)
# print(talaba1.see_methods())






# Kod_16
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.sinf = 1
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya} {self.tyil}-was born in. Kimyo International University In Tashkent {self.sinf}-stage student "

#     def see_methods(self):
#         return [method for method in self.__dict__ if not method.startswith('__')]


# talaba1 = Talaba("Xusanbek", "Suyunov", 2005)
# print(talaba1.see_methods())
