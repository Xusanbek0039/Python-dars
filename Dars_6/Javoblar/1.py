my_family = ["Ota", "Ona", "Ukam", "Singlim", "Men"]

print("Oila azolari:")
for member in my_family:
  print(member)

print(f"\nOila azolari soni: {len(my_family)}")

print("\nTartiblangan ro'yxat:") 
for member in sorted(my_family):
  print(member)

print("\nTeskari tartibdagi ro'yxat:")
for member in reversed(my_family): 
  print(member)