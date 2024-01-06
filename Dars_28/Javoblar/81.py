"""Seaborn kutubxonasidan foydalangan holda erkin dastur yozing. 
Kutubxona haqida internetdan malumotlar qidirib koring hamda o’sha olgan malumotlaringizdan foydalangan holda kod yozing.
Darslikda foydalanilgan kodl;ardan foydalanmang."""
from numpy import random   #  numpy qilib oldik
import matplotlib.pyplot as plt  #    import qilib olib 
import seaborn as sns   #   importga seaborni yozib oldim

sns.distplot(random.normal(loc=40, scale=9, size=9888), hist=True, label='poisson') #40,  9888  poisson
sns.distplot(random.poisson(lam=60, size=9765), hist=True, label='normal')   #distplot qilib 60, 9765,    normal

plt.show()  # javobni show ga yuklab javobni chiqaryabmiz

