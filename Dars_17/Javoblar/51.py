"""
Foydalanuvchidan aylaning radiusini qabul qilib olib, 
uning radiusini, diametrini, perimetri va yuzini lug'at 
ko'rinishida qaytaruvchi funksiya yozing

"""



pi = 3.1415926

def get_circle_info(radius):
    diameter = 2 * radius
    perimeter = 2 * pi * radius  
    area = pi * radius * radius
    
    circle_info = {
        "radius": radius,
        "diameter": diameter,
        "perimeter": perimeter, 
        "area": area
    }
    
    return circle_info

circle = get_circle_info(5)
print(circle)