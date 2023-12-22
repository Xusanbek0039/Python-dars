"Pythonda Fayllar bilan bo'limi"

# Kod_1
# f = open("myfile.txt")   #open = ochmoq
# print(f.read())       #read = o'qimoq





# # Kod_2
# with open("myfile.txt", "a") as file:   #open writh = zudlik bilan ochish(holat bo'lib kelmoqda )
#     file.write("Yangi ma'lumotlar")


# f = open("myfile.txt")   #open = ochmoq
# print(f.read())       #read = o'qimoq






# # KOd_3
# with open("myfile.txt", "w") as file:
#     file.write("Ma'lumotlar")

# f = open("myfile.txt")   #open = ochmoq
# print(f.read())       #read = o'qimoq






# Kod_4
# with open("myfile.txt", "w") as file:
#     file.write("Ma'lumotlar")
# with open("myfile.txt", "w") as file:
#     file.write("Satr 1\n")
#     file.write("Satr 2\n")
#     file.write("Satr 3\n")


# f = open("myfile.txt")   #open = ochmoq
# print(f.read())       #read = o'qimoq



# # Kod_5
# try:
#     with open("myfile.txt", "x") as file:
#         # Faylga ma'lumot yozish va boshqa amallar
#         file.write("Yangi ma'lumotlar")
# except FileExistsError:
#     print("Fayl allaqachon mavjud.")





# # Kod_6
# with open("myfile.txt", "rt") as file:
#     data = file.read()
#     print(data)




# Kod_7
# with open("image.jpg", "rb") as file:
#     data = file.read()
#     # Ikkilik ma'lumotlar bilan ishlovchi amallar



# Kod_8
# try:
#     file = open("C:/Users/user/Downloads/myfile.txt", "r")  #bu yerda C:/Users/user/Downloads/myfile.txt manzil hisoblanadi
#     # Faylning o'qish bilan biror ishni amalga oshirish mumkin
#     print(file.read())

# except FileNotFoundError:   #agarda fayl yoq bolsa 
#     print("Fayl topilmadi.")
