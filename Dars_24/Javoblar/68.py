"""Topshiriq:
Python dasturlash tilida class  mavzusida erkin dastur yozing:"""

class Talaba:    # Talaba degan class olib oldik
    def __init__(self,ism,familiya,yosh):    #init qilib ismini  familiyasini yoshini yozdim
        self.ism=ism   # selfda ismini yozdim
        self.familiya=familiya # selfda familiyasini yozdim
        self.yosh=yosh  # selfda yoshini yozdim
    def get_fullname(self):  #def qilib oldik
        return f"{self.ism} {self.familiya} {self.yosh}-yoshda"  # returnda self qilib familiyasini va yoshini chiqarib oldik
n=Talaba("Ergashev","Donyor",27) # o'zgaruvchiga Talaba deb yashini va  ismini familiyasini kiritib oldik
print(n.get_fullname())   # javobini chiqarib oldik