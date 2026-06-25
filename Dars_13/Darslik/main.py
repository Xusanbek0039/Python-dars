# 1-masala
# text = input("Matin kiriting: ")
# soz = text.split()
# soz_lugat = {}



# for word in soz:
#     soz_lugat[word] = soz_lugat.get(word, 0) + 1

# print(soz_lugat)






# 2-masala
# text = input("Matin kiriting: ")
# soz = text.split()
# soz_lugat = {}

# for word in soz:
#     soz_lugat[word] = soz_lugat.get(word, 0) + 1

# x = max(soz_lugat, key=soz_lugat.get)
# print(f"Eng ko‘p uchragan so‘z: {x} ({soz_lugat[x]} marta)")





# 3-masala
# grades = {
#     "Ali": 85, 
#     "Vali": 92, 
#     "Zarina": 78, 
#     "Olim": 90, 
#     "Madina": 95
#     }

# max_baxo = max(grades,key=grades.get)
# min_baxo = min(grades, key=grades.get)
# qiymat = sum(grades.values()) / len(grades)

# print(f"Eng yuqori ball: {max_baxo} ({grades[max_baxo]})")
# print(f"Eng past baxo: {min_baxo} ({grades[min_baxo]})")
# print(f"O'rtacha baxo: {qiymat}")










# 4-masala
# students = { 
#     "Ali": {"Math": 90, "English": 85, "Science": 88}, 
#     "Vali": {"Math": 75, "English": 80, "Science": 78}, 
#     "Zarina": {"Math": 95, "English": 92, "Science": 89} 
# }

# qiymat = {student: sum(ball.values()) // len(ball) for student, ball in students.items()}
# print(qiymat)






# 5-masala
# dict1 = {"a": 10, "b": 20, "c": 30} 
# dict2 = {"b": 5, "c": 15, "d": 25}

# x = dict1.copy()
# for key,qiymat in dict2.items():
#     x[key] = x.get(key,0) + qiymat

# print(x)







# 6-masala 
# sonlar = [1, 2, 2, 3, 3, 3, 4]
# noyob = list(set(sonlar))

# print(noyob)





'''
MASALA 
========================================
Quyidagi lug'at berilgan:
students = {
    "Ali": ["Python", "Django", "HTML", "CSS", "Python"],
    "Vali": ["HTML", "CSS"],
    "Zarina": ["Python", "Django", "JavaScript", "HTML"],
    "Madina": ["Python", "Python", "Django", "HTML", "CSS", "JavaScript"]
}
Vazifa:
Har bir o'quvchi nechta noyob kurs o'qiyotganini toping.
Natijani yangi lug'atga saqlang.
Eng ko'p noyob kurs o'qiyotgan o'quvchini toping.
Agar bir nechta o'quvchida bir xil maksimal qiymat bo'lsa, birinchisini chiqarish kifoya.

Natija:

Ali -> 4 ta kurs
Vali -> 2 ta kurs
Zarina -> 4 ta kurs
Madina -> 4 ta kurs

Eng faol o'quvchi: Ali (4 ta kurs)
'''