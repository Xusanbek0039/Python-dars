# -*- coding: utf-8 -*-
from _pdf_engine import make_lesson
make_lesson("_test.pdf", 1, "Python bilan tanishuv va print()",
  "Birinchi dastur, ekranga ma'lumot chiqarish va f-string",
  [
    ("h2","1. Python nima?"),
    ("p","Python — bu o'rganish oson, kuchli va keng tarqalgan dasturlash tili. Unda **veb-saytlar**, **sun'iy intellekt**, **o'yinlar** va avtomatlashtirish dasturlari yoziladi."),
    ("bul",["Sintaksisi sodda va o'qishga qulay","Bepul va ochiq manbali","Katta kutubxonalar to'plamiga ega"]),
    ("h2","2. Birinchi dastur"),
    ("p","Ekranga matn chiqarish uchun `print()` funksiyasidan foydalanamiz:"),
    ("code","print(\"Salom dunyo\")","Natija: Salom dunyo"),
    ("note","Matn (string) ikki tirnoq \" \" yoki bitta tirnoq ' ' ichida yoziladi."),
  ])
print("OK")
