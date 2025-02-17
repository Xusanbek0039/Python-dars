# 1-masala
# n = int(input("Son kiriting: "))
# if n % 2 == 0:
#     print("Bu son juft.")
# else:
#     print("Bu son toq.")







# 2-masala
# n = int(input("Son kiriting: "))
# print(f"Kvadrat: {n**2}, Kub: {n**3}")




# 3-masala
# a = int(input("Birinchi son: "))
# b = int(input("Ikkinchi son: "))
# print(f"Kattasi: {max(a, b)}")






# 4-masala
# n = int(input("N sonini kiriting: "))
# yigindi = sum(range(1, n+1))
# print(f"Yig‘indi: {yigindi}")












# 5-masala
n = int(input("Nechta Fibonachchi soni kerak? "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])
print(fib[:n])





















# 6-masala
# soz = input("So‘z kiriting: ")
# print(soz[::-1])





# 7-masala
# sonlar = [12, 45, 78, 2, 56, 89, 23]
# print(f"Eng katta: {max(sonlar)}, Eng kichik: {min(sonlar)}")




# 8-masala
# matn = input("Matn kiriting: ")
# unlilar = "aeiouAEIOU"
# print("".join([harf for harf in matn if harf in unlilar]))




# 9-masala
# sonlar = [-10, 20, -30, 40, -50, 60]
# print([x for x in sonlar if x > 0])





# 10-masala
# # Oila a'zolarining ro‘yxatini yaratamiz
# my_family = ["Ali", "Vali", "Hasan", "Husan", "Olim"]

# # Oila a'zolarining ismlarini ekranga chiqaramiz
# print("Oila a'zolari:")
# for ism in my_family:
#     print(ism)

# # Nechta oila a'zosi borligini hisoblaymiz
# print(f"\nOilamizda {len(my_family)} ta a'zo bor.")

# # Ro‘yxatni alifbo bo‘yicha tartiblaymiz
# sorted_family = sorted(my_family)
# print("\nAlifbo tartibida:")
# print(sorted_family)

# # Ro‘yxatni teskari tartibda chiqaramiz
# print("\nTeskari tartibda:")
# print(sorted(my_family, reverse=True))

