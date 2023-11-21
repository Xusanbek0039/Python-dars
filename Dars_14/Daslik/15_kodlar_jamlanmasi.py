#Kod_1
# i = 1   
# while i<=6:
#     print(i)
#     i+=1














# #Kod_2    whileda masala 
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
















#Kod_3   flag tushunchasi
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)


















#Kod_4 break tushunchasi
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)












# Kod_5     break operatori for da 
# sonlar = list(range(1,11))
# for son in sonlar: 
#     if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")












# #Kod_6   for da continue 
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")





#Kod_7     while da contiune
# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)





#Kod_8    abadiy tsikl
# son = 0
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son)





#Kod_9
# son = 0
# while son<10:    
#     if son%2!=0:
#         continue
#     else:
#         print(son)
#     # son += 1







# Kod_10
# son = 1
# while son>0: 
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)