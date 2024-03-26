kutubxonalar = ["NumPy", "Random", "Seaborn", "Math","exit"]

for kutubxona in kutubxonalar:
    kutubxona_nom = input("Kutubxona nomini kiriting: ")
    if kutubxona_nom in kutubxonalar:
        print(f"{kutubxona_nom} kutubxonasi haqida ma'lumotlar:")
        # Kutubxona haqida ma'lumotlarni chiqaring
        if kutubxona_nom == 'exit':
            break
        if kutubxona_nom == "NumPy":
            print("NumPy haqida malumotlar yuklash uchun joy.")
            # NumPy kutubxonasi haqida boshqa ma'lumotlar
        elif kutubxona_nom == "Random":
            print("Random haqida malumotlar joylash uchun joy.")
        else:
            print(f"{kutubxona_nom} ushbu kutubxona xaqida malumot topilmadi.")
    else:
        print("Bunday kutubxona nomi yo'q.")

print("Biz bilan bo'lganingiz uchun tashakkur!")
