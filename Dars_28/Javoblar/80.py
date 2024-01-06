"""Random hamda NumPy kutubxonalaridan foydalangan holda erkin dastur yozing.
Dastur davomida darsliklarda foydalanilmagan kodlardan foydalanmang. """

from numpy import random 

t = random.poisson(lam=9, size=100)

n=random.rand(98)    # rand 98 ning o'nlik sonnini  oladi float sonini

l=random.poisson(lam=67,  size=800) 

u=random.rand(86)     #rand  soning ihtiyiriy float soni yani o'nlik sonni oladi 86 

j=random.randint(567)    # randind 567 oralig'idagi soni ko'rsatadi

x=random.randint(498)    # randint sonlarning orasidagi soni chiqaradi 498 ning oralig'idagi sonlarni chiqaradi

p=random.poisson(lam=98, size=765)  # p deb 98, 765 deb yozdim

print(t,n,u,j,x)  # javobni printga chiqardik