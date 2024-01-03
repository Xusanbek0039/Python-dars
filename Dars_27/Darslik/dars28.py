"""Dars 28 kodlar jamlanmasi:
Quyidagi darsda siz OS hamda Numpy kutubxonalari bilan ishlashni o'rganasiz."""


# Kod_1
# import os
# os.remove("myfile.txt")






# Kod_2
# import os

# moyfile = "myfile.txt"

# with open(moyfile, "w") as fayl:
#     fayl.write("")

# if os.path.exists(moyfile):
#     print("myfile nomli fayl muvafaqiyatli yaratildi")
# else:
#     print("myfile nomli fayl yaratilmadi")





# Kod_3
# import os

# my_file = "myfile.txt"

# if os.path.exists(my_file):
#     os.remove(my_file)
#     print("Fayl muvaffaqiyatli o'chirildi")
# else:
#     print("Fayl topilmadi")








# Kod_4
# import os

# papka_nomi = "myfile"              #yaratmoqchi bo'lgan papkamizga nom berib olindi

# try:
#     os.mkdir(papka_nomi)                  #mkdir pythonda papka yaratishda ishlatilinadi
#     print("Yangi papka muvaffaqiyatli yaratildi.")      #agar papka yaratilinsa 
# except OSError as error:                                   #OSError yoki error bu yerda modulda xatolik ham kuzatilingani sababli yozilmoqda 
#     print(f"Papka yaratishda xatolik yuz berdi: {error}") #agar papka yaratilinmasa yoki mavjud bo'lsa 



# # Kod_5
# import os

# my_folder = "myfile"

# if os.path.exists(my_folder):     #agar os yoli boyicha berilgan papka mavjud bolsa uni yoq qil
#     os.rmdir(my_folder)             #rmdir papka o'chirishda  qo'llaniladi bu usulni os kutubxonasidan foydalanmagan holda qo'llahsimiz ham mumkin
#     print("Fayl muvaffaqiyatli o'chirildi")     #papka muvafaqiyatli o'chirilsa
# else:
#     print("Fayl topilmadi")          #agarda papka  topilmasa 








# Kod_6
# # import numpy as np

# # print(np.__version__)


# import numpy
# print(numpy.__version__)






# Kod_7
# import numpy as np

# x = np.array([1, 2, 3, 4, 5])   #array =  massiv

# print(x)

# print(type(x))





# # Kod_8
# import numpy as np

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)







# Kod_9
# import numpy as np

# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print("O'lchamlar soni :", arr.ndim)






# # Kod_10
# import numpy as np

# arr = np.array([1, 2, 3, 4])

# print(f"0- indeks {arr[0]} ga teng")






# # Kod_11
# import numpy as np

# arr = np.array([1, 2, 3, 4])

# print(arr[2] + arr[3])






# # Kod_12
# import numpy as np

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('1-qatordagi 2-element:', arr[0, 1])




# # Kod_13
# import numpy as np

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('2- qatordagi 5- element ', arr[1, 4])





# Kod_14
# import numpy as np

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(arr[0, 1, 2])