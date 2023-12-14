"""Python dasturlash tilida interatorlar:"""
# Darslik Python 3.10 hamda undan yuqori versiyali uchun ishlab chiqarilgan:

#@IT_Creative uchun mahsus
# Kod_1
# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))






# Kod_2
# my_list = [1, 2, 3, 4, 5]
# my_iterator = iter(my_list)

# print(next(my_iterator))  # 1
# print(next(my_iterator))  # 2
# print(next(my_iterator))  # 3
# print(next(my_iterator))  # 4
# print(next(my_iterator))  # 5
# print(next(my_iterator))  # StopIteration xatosi






# Kod_3
# mystr = "banana"
# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))




# Kod_4
# mytuple = ("apple", "banana", "cherry")

# for x in mytuple:
#   print(x)







# Kod_5
# mytuple = ("apple", "banana", "cherry")
# length = len(mytuple)
# i = 0

# while i < length:
#     x = mytuple[i]
#     print(x)
#     i += 1







# Kod_6
# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))





# Kod_7
# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#   print(x)





class OddNumbers:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration
        else:
            result = self.current
            self.current += 2
            return result

# Iterator obyektini yaratish
odd_numbers = OddNumbers(10)

# Iteratsiya orqali tek sonlarni chop etish
for number in odd_numbers:
    print(number)
