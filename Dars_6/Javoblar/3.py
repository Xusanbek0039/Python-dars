taomlar = ["Osh", "Manti", "Shashlik", "Lag'mon", "Qozon kabob"]

print("Barcha taomlar: ")
print(taomlar)

nonushta = taomlar[:] # taomlar ro'yxatidan nusxa olish

nonushta.remove("Osh")
nonushta.remove("Shashlik")
nonushta.remove("Qozon kabob")
nonushta.append("Qaymoq")
nonushta.append("Uzoq")

print("\nNonushtaga yeyiladigan taomlar:")
print(nonushta)