def aylana_hisobla(radius):
    # Radiusni hisoblash
    radius = float(radius)

    # Diametrni hisoblash
    diametr = 2 * radius

    # Perimetrdagi uzunligini hisoblash
    perimetri = 2 * 3.14159 * radius

    # Yuzini hisoblash
    yuzi = 3.14159 * radius ** 2

    # Lug'atni tuzish va qiymatlarni joylash
    lugat = {
        'radius': radius,
        'diametr': diametr,
        'perimetri': perimetri,
        'yuzi': yuzi
    }

    return lugat

# Foydalanuvchidan radiusni olish
radius = input("Aylaning radiusini kiriting: ")

# Aylana haqida ma'lumotlar
aylana_malumotlari = aylana_hisobla(radius)

# Natijalarni chiqarish
print("Aylana haqida ma'lumotlar:")
print("Radius: ", aylana_malumotlari['radius'])
print("Diametr: ", aylana_malumotlari['diametr'])
print("Perimetri: ", aylana_malumotlari['perimetri'])
print("Yuzi: ", aylana_malumotlari['yuzi'])