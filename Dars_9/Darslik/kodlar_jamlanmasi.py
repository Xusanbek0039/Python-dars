# # 1-kod
# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#    print('Sizga kirish bepul.')
   
# elif yosh <= 12:
#    print('Sizga kirish 5000 so\'m')
   
# else:
#    print('Sizga kirish 10000 so\'m')












# kod_2
# yosh = int(input('Yoshingiz nechida? '))

# if yosh <= 4:
#    x = 0
   
# elif yosh <= 12:
#    x = 5_000
   
# else:
#    x = 10_000
   
# print(f"Sizga kirish {x} so'm")











# # kod_3
# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4: # yosh bolalarga bepul
#    price = 0
# elif yosh <= 12: # 4 dan 12 yoshgacha 5000 so'm
#    price = 5000
# elif yosh < 65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
#    price = 10000
# elif yosh < 90: # qariyalarga esa 8000 so'm
#    price = 8000
# else:
#     price = 15_000
# print(f"Sizga kirish {price} so'm")













# # Kod_4
# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#    price = 0
# elif yosh<=12:
#   price = 5000
# elif yosh<65:
#    price = 10000
# elif yosh>=65:
#    price = 8000   
# print(f"Sizga kirish {price} so'm")















# # Kod_5
# kun = input("Bugun nima kun?>>> ")

# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#    print(f"Bugun {kun.title()}, dam olish kuni.")
   
# elif kun.lower() == 'dushanba' or kun.lower() == 'seshanba' or kun.lower() == 'chorshanba' or kun.lower() == 'payshanba' or kun.lower() == "juma":
#     print(f"Bugun {kun.title()}, ish kuni!")
    
# else:
#    print('Siz xafta kunini kiritishda xatolikka yo`l qo`ydingiz!')















# # Kod_6
# kun = input("Bugun nima kun? ")
# harorat = float(input("Havo harorati qanday? "))
# if kun.lower()=='yakshanba' and harorat >= 30:
#    print("Cho'milgani ketdik!")
   
# elif kun.lower()=='yakshanba' and harorat<30:
#    print("Uyda dam olamiz!")
   
# elif kun.lower()=='shanba' and harorat >= 30:
#    print("Cho'milgani ketdik!")
   
# else:
#    print("Bugun ish kuni ekan!")















# # Kod_7
# kun = input("Bugun nima kun? ")
# harorat = float(input("Havo harorati qanday? "))

# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat >= 30:
#    print("Cho'milgani ketdik!")
   
# elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat < 30:
#    print("Uyda dam olamiz!")

















# # Kod_8
# narh = 15_000 # mijoz 15000 so'mga taom oldi.
# choy = True # mijoz choy ham oldi
# salat = True # mijoz salat olmadi

# if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
#    narh = narh + 10000 # narhga 10000 so'm qo'shamiz
# elif choy or salat: # agar choy yoki salat olgan bo'lsa
#    narh = narh + 5000 # narhga 5000 so'm qo'shamiz
#    print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz                                 














# # Kod_9
# narh = 15000 # mijoz 15 so'mga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = True
# #Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# if choy:   # agar choy olsa
#    print("Mijoz choy oldi.")
#    narh = narh + 3000
# if salat:  # agar salat olsa
#    print("Mijoz salat oldi.")
#    narh = narh + 5000
# if non:    # agar non olsa
#    print("Mijoz non oldi.")
#    narh = narh + 2000
# if kompot: # agar kompot olsa
#    print("Mijoz kompot oldi.")
#    narh = narh + 5000
# if assorti: # agar assorti olsa
#    print("Mijoz assorti oldi.")
#    narh = narh + 15000
  
# print(f"Jami {narh} so'm")















# # Kod_10
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>> ')
# if ovqat.lower() in menu:
#    print('Buyurtma qabul qilindi.')
# else:
#    print(f"Afsuski siz buyurgan {ovqat.title()} bizning taomnomamizda mavjud emas!")












# # Kod_11
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() not in menu:
#    print('Afsuski bizda bunday ovqat yo\'q')
# else:
#    print('Buyurtma qabul qilindi.')

















# # Kod_12
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]                               

# for taom in buyurtmalar:
#    if taom in menu:
#        print(f"Menuda {taom} bor")
#    else:
#        print(f"Kechirasiz, menuda {taom} yo'q")















# # Kod_13
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ['osh',"manti"]

# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f"Menuda {taom} bor")
#        else:
#            print(f"Kechirasiz, menuda {taom} yo'q")
# else: # agar ro'yxat bo'sh bo'lsa
#    print("Savatchangiz bo'sh!")
#############################################################################
n = int(input("Hurmatli mijoz siz nechta taom buyurtma qilmoqchisiz\t"))
menu = ['osh','shashlik','manti','somsa','qozonkabob','tandir','shorva']
buyurtmalar = []
for i in range(0,n):
    buyurtma = input(f"{i+1}-buyurtmani kiriting:\t")
    buyurtmalar.append(buyurtma.lower())


for taom in buyurtmalar:
    if taom in menu:
        print(f"\nSiz kiritgan {taom.title()} taomiga buyurtma berildi!")
    else:
        print(f"\nSiz kiritgan {taom.title()} taomi afsuski bizda mavjud emas!")
        
print(f"\nSiz {len(buyurtmalar)} ta buyurtma berdingiz!")