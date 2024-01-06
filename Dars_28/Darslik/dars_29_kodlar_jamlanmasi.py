"""Random hamda NumPy bilan ishlash"""


# Kod_1
# from numpy import random

# x = random.randint(100)

# print(x)







# # Kod_2
# from numpy import random

# x = random.rand()    #rand float son qaytaradi

# print(x)







# # Kod_3
# from numpy import random

# x=random.randint(100, size=(5))     # size o'lcham beradi

# print(x)






# KOD_4
# from numpy import random

# x = random.randint(100, size=(3, 5))

# print(x)







# # Kod_5
# from numpy import random

# x = random.rand(5)

# print(x)






# Kod_6
# from numpy import random

# x = random.rand(3, 5)

# print(x)







# KOd_7
# from numpy import random

# x = random.choice([3, 5, 7, 9])

# print(x)







# # Kod_8
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot([0, 1, 2, 3, 4, 5])    #distplat chizma chizuvchi oynani chaqiruvchi seaborn kutubxonasi bir funksiyasi

# plt.show()       #seaborn kutubxonasini korish uchun shu buyruq ishlatilinadi. show = korsatish 








# Kod_9
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot([0, 1, 2, 3, 4, 5], hist=False)   

# plt.show()







#Kod_10
# import numpy as np

# # Normal o'rindiqdan tasodifiy qiymatlarni generatsiyalash
# mean = 0  # O'rta qiymat
# std_dev = 1  # Dispersiya (standart chetlashgan qiymat)

# # Tasodifiy 10 ta qiymat generatsiyalash
# random_values = np.random.normal(mean, std_dev, 10)

# print(random_values)






# Kod_11
# def locate_city(city):
#     if city == ('Toshkent'):
#         print("Toshkent Oʻzbekistonning poytaxti.")
#     elif city == 'Paris':
#         print("Parij - Fransiyaning poytaxti.")
#     elif city == 'New York':
#         print("Nyu-York AQShning yirik shahri.")
#     else:
#         print("Shahar haqida ma'lumot mavjud emas.")

# # 'Tashkent' uchun joylashuv ma'lumotini olish
# locate_city('Toshkent')

# # 'London' uchun joylashuv ma'lumotini olish
# locate_city('London')







# # Kod_12
# import numpy as np

# def standart_orindiq_taqsimoti_kesishmasi(mean, std_dev, num_deviations):
#     pastki_chegarali = mean - num_deviations * std_dev
#     yuqori_chegarali = mean + num_deviations * std_dev
#     return pastki_chegarali, yuqori_chegarali

# # O'rta qiymat va dispersiya
# orta_qiymat = 0
# dispersiya = 1

# # 68% yotganlik miqdorining kesishmasi
# pastki, yuqori = standart_orindiq_taqsimoti_kesishmasi(orta_qiymat, dispersiya, 1)
# print("68% yotganlik miqdorining kesishmasi:", pastki, "-", yuqori)

# # 95% yotganlik miqdorining kesishmasi
# pastki, yuqori = standart_orindiq_taqsimoti_kesishmasi(orta_qiymat, dispersiya, 2)
# print("95% yotganlik miqdorining kesishmasi:", pastki, "-", yuqori)

# # 99.7% yotganlik miqdorining kesishmasi
# pastki, yuqori = standart_orindiq_taqsimoti_kesishmasi(orta_qiymat, dispersiya, 3)
# print("99.7% yotganlik miqdorining kesishmasi:", pastki, "-", yuqori)







# # KOd_13
# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# size = arr.size

# print("Massivning umumiy elementlar soni:", size)








# Kod_14
# import numpy as np

# n = 10  # Sinovlar soni
# p = 0.5  # Har bir sinovning yuzaga kelish ehtimoli
# size = 5  # Massivning shakli

# binomial_distribution = np.random.binomial(n, p, size)
# print("Binom taqsimoti natijalari:", binomial_distribution)




# Kod_15

# import numpy as np

# # Diskret o'zgaruvchilar
# tashkilotlar = ['A', 'B', 'C', 'D', 'E']
# foizlar = [10, 20, 30, 25, 15]

# # Diskret taqsimot (CategoriDistribution)
# tashkilot_taqsimoti = np.random.choice(tashkilotlar, p=foizlar/np.sum(foizlar), size=100)

# # Taqsimot natijalarini hisoblash
# tashkilotlar_soni = [np.sum(tashkilot_taqsimoti == tashkilot) for tashkilot in tashkilotlar]

# # Natijalarni chiqarish
# for tashkilot, son in zip(tashkilotlar, tashkilotlar_soni):
#     print(tashkilot, ": ", son)






# Kod_16
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

# plt.show()






# # Kod_17
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
# sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

# plt.show()






# Kod_18_1
# import numpy as np

# # Lambda qiymati
# lam = 2

# # Puasson taqsimoti natijalari
# puasson_taqsimoti = np.random.poisson(lam, size=100)

# # Natijalarni chiqarish
# for natija in puasson_taqsimoti:
#     print(natija)





# # Kod_18_2
# from numpy import random

# x = random.poisson(lam=2, size=10)

# print(x)








# # Kod_19
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot(random.poisson(lam=2, size=1000), kde=False)

# plt.show()






# # Kod_20
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
# sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

# plt.show()




# Kod_21
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')

plt.show()