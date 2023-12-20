"26-dasr-kodlar-jamlanmasi"  



# Kod_1
# import re

# matn = "Men Python dasturlash tilini o'rganaman."
# qidiruv = r"Python"

# natija = re.search(qidiruv, matn)

# if natija:
#     print("Qidiruv natijasi topildi.")
# else:
#     print("Qidiruv natijasi topilmadi.")








# # Kod_2
# import re

# matn = input("Iltimos, qidirish uchun matn kiriting: ")
# qidiruv = r"python"

# natija = re.search(qidiruv, matn)

# if natija:
#     print("Qidiruv natijasi topildi.")
# else:
#     print("Qidiruv natijasi topilmadi.")








# Kod_3
# import re

# soz = input("So'z kiriting: ")
# sher = """
# O, ota makonim. Onajon o‘lkam,
# O’zbekiston, jonim to‘shay soyangga.
# O, ota makonim. Onajon o‘lkam,
# O’zbekiston, jonim to‘shay soyangga.
# Senday mehribon yo‘q,
# Seningdek ko‘rkam.
# Rimni alishmasman bedapoyangta.

# Bir go‘sha suv bo‘lsa, bir go‘sha qirlar,
# Qancha yurtni ko‘rdim, qancha taqdirlar.
# Qayga borsam suyab, boshni tik tut deb,
# Tog‘laring ortimdan ergashib yurar.

# Ko‘rdim suluvlarning eng faranglarin.
# Yo xudbinman men yo bir sodda kasman men –
# Parijning eng go‘zal restoranlarin,
# Bitta tandiringga alishmasman men.

# Na gapga ko‘nayin, Na til bilayin,
# Ko‘zdan uyqu qochdi, dildan halovat -
# Uch kunda sog‘insam nima qilayin,
# Chala qolar bo‘ldi hamma sayohat.

# Bildimki, baridan ulug‘im o‘zing,
# Bildimki, yaqini shu tuproq menga.
# Bahorda Baxmalda tug‘ilgan qo‘zing,
# Arab ohusidan azizroq menga.

# Sen bilan o‘tgan har kun bayram - bazm,
# Sensiz bir on qolsam vahmim keladi.
# Seni bilganlarga qilaman ta’zim,
# Seni bilmaslarga rahmim keladi.
# """

# # Berilgan sozni qidirish
# match = re.search(rf'\b{soz}\b', sher, re.IGNORECASE)

# if match:
#     print(f"{match.group()} so'zi bizning sherimizda mavjud!")
    
# else:
#     print(f"Siz kiritgan soz qidiruvda topilmadi!")







# # Kod_4
# import re

# soz = input("So'z kiriting: ")
# sher = """
# O, ota makonim. Onajon o‘lkam,
# O’zbekiston, jonim to‘shay soyangga.
# O, ota makonim. Onajon o‘lkam,
# O’zbekiston, jonim to‘shay soyangga.
# Senday mehribon yo‘q,
# Seningdek ko‘rkam.
# Rimni alishmasman bedapoyangta.

# Bir go‘sha suv bo‘lsa, bir go‘sha qirlar,
# Qancha yurtni ko‘rdim, qancha taqdirlar.
# Qayga borsam suyab, boshni tik tut deb,
# Tog‘laring ortimdan ergashib yurar.

# Ko‘rdim suluvlarning eng faranglarin.
# Yo xudbinman men yo bir sodda kasman men –
# Parijning eng go‘zal restoranlarin,
# Bitta tandiringga alishmasman men.

# Na gapga ko‘nayin, Na til bilayin,
# Ko‘zdan uyqu qochdi, dildan halovat -
# Uch kunda sog‘insam nima qilayin,
# Chala qolar bo‘ldi hamma sayohat.

# Bildimki, baridan ulug‘im o‘zing,
# Bildimki, yaqini shu tuproq menga.
# Bahorda Baxmalda tug‘ilgan qo‘zing,
# Arab ohusidan azizroq menga.

# Sen bilan o‘tgan har kun bayram - bazm,
# Sensiz bir on qolsam vahmim keladi.
# Seni bilganlarga qilaman ta’zim,
# Seni bilmaslarga rahmim keladi.
# """

# # Berilgan sozni qidirish
# matches = re.findall(rf'\b{soz}\b', sher, re.IGNORECASE)

# if matches:
#     print(f"'{soz}' sozi {len(matches)} marta ishlatilgan:")
    
# else:
#     print("Berilgan soz topilmadi.")





# # Kod_5
# try:
#   print(x)
# except:
#   print("Xatolik yuz berdi. Yani x qiymat topilmadi.")









# # Kod_6
# x = "Dastur xatosiz ishlamoqda !"
# try:
#   print(x)
# except:
#   print("Xatolik yuz berdi. Yani x qiymat topilmadi.")







# Kod_7
# try:
#   print(x)
# except:
#   print("Nimadir noto'g'ri bajarildi")
# finally:
#   print("Urinishdan tashqari tugadi")






# # kod_8
# try:
#     x = 10
#     print(x)  # x ni chop etish
# except:
#     print("Nimadir noto'g'ri bajarildi")
# finally:
#     print("Dastur xatosiz ishladi")


