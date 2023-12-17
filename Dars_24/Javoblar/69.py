"""Topshiriq:
Python dasturlash tilida kutubxonalar mavzusida ixtiyoriy dastur yozing:
misol uchun joriy yilni chiroyli ko’rinishda chiqaruvchi yoxud matematik amallar bajaruvchi dastur."""
import datetime #inport =ko'chirib kelish degan manoni anglatadi  datetime= sana vaqt degan manoni anglatadi

x=datetime.datetime.now()   #now =hozir  deyiladi

print(f"Joriy yil {x.year}")    # year=yil  deyiladi
print(x.strftime("%h"))          #strftime -datetime moduli funksiyasi   deyiladi
