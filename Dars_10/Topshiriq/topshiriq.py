"""
1-masala
Foydalanuvchi baho kiritadi. Dastur ushbu bahoga qarab 
quyidagi natijani chiqaradi:

90 dan katta bo‘lsa → "A"
80 dan katta bo‘lsa → "B"
70 dan katta bo‘lsa → "C"
60 dan katta bo‘lsa → "D"
Aks holda → "F"
"""














# score = int(input("Baxoni kiriting: "))

# if score >= 90:
#     print(score, "→ A")
# elif score >= 80:
#     print(score, "→ B")
# elif score >= 70:
#     print(score, "→ C")
# elif score >= 60:
#     print(score, "→ D")
# else:
#     print(score, "→ F")






"""
    2-masala
    Qabul qilingan sonni 
    Agar son 3 ga bo‘linsa → "Fizz"
    Agar son 5 ga bo‘linsa → "Buzz"
    Agar son 3 hamda 5 ga bo‘linsa → "FizzBuzz"
    Aks holda sonning o‘zi chiqarilsin.
"""








# i = int(input("Son kiriting: "))

# if i % 3 == 0 and i % 5 == 0:  
#     print("FizzBuzz")  
# elif i % 3 == 0:  
#     print(f"Fizz {i}")  
# elif i % 5 == 0:  
#     print(f"Buzz {i}")  
# else:  
#     print(i)  


"""
3-masala
Foydalanuvchi kiritgan matndagi unli harflarni 
sanaydigan dastur yozing.
"""











matin = "Python dasturlash tili"  
unlilar = "aeiouAEIOU"  
son = 0  

for raqam in matin:  
    if raqam in unlilar:  
        son = 1 + son

print("Unli harflar soni:", son)  







"""
4-masala
Berilgan ro‘yxatdagi sonlarning o‘rtacha 
qiymatini hisoblovchi dastur yozing.
"""
sonlar = []
for i in range(5):
    son = int(input(f"{i+1}-sonni kiriting: "))
    sonlar.append(son)

bolish = len(sonlar)
summ = 0
for raqam in sonlar:
    summ += raqam


print(f"{sonlar} yigindisi {summ} o'rtacha qiymati {summ//raqam}")




numbers = [12, 45, 78, 34, 56, 89, 23]  
sum_numbers = 0  

for num in numbers:  
    sum_numbers += num  

average = sum_numbers / len(numbers)  
print("O‘rtacha qiymat:", average)  
