"""Foydalanuvchidan son qabul qilib, shu son miqdoricha 
Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi 
funksiya yozing. Ta’rif: Har bir hadi o’zidan oldingi 
ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik 
Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish 
had ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 
34, 55,..."""


def fibonacci(n):
    numbers = []
    a, b = 0, 1
    
    for i in range(n):
        numbers.append(b) 
        a, b = b, a+b
        
    return numbers

print(fibonacci(10))