# -*- coding: utf-8 -*-
"""
Created on Tue May  2 15:48:24 2023

@author: Kamalov M
"""

#20:48 02.05.2023
#23-dars>>>MODULLAR


def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rangi':rangi,
            'korobka':korobka,
            'yil':yili,
            'narhi':narhi}
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlar bit"""
    avtolar=[] #salondagi bosh avtolar uchun ro'yxat
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting:" , end=' ')
        kompaniya=input("Ishlab chiqaruvchi:>>")
        model = input("Modeli:>>")
        rangi=input("Rangi:>>")
        korobka=input("Korobka:>>")
        yili= input("Ishlab chiqarilgan yili:>>")
        narhi=input("Narhi:>>")
        
        
def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi dastur"""
    print(f"{avto_info['rangi'].title()} {avto_info['kompaniya'].upper()}"
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narhi']} $")