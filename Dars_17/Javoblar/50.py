"""Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. 
Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, 
el.manzil)"""


def get_user_info(ism, familiya, tugilgan_yil, tugilgan_joy, email=None, tel=None):
    user_info = {}
    user_info['ism'] = ism
    user_info['familiya'] = familiya
    user_info['tugilgan_yil'] = tugilgan_yil
    user_info['tugilgan_joy'] = tugilgan_joy
    user_info['yosh'] = 2023 - tugilgan_yil
    
    if email:
        user_info['email'] = email
        
    if tel:
        user_info['tel'] = tel
        
    return user_info

user1 = get_user_info('Ali', 'Valiyev', 2000, 'Toshkent') 
user2 = get_user_info('Hasan', 'Alimov', 1995, 'Farg\'ona', 'hsnalimov@mail.ru', '+99897123456')

print(user1)
print(user2)