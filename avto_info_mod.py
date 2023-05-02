# -*- coding: utf-8 -*-
"""
Created on Tue May  2 15:48:24 2023

@author: Kamalov M
"""

#20:48 02.05.2023
#23-dars>>>MODULLAR


def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    """Avtomobil haqidagi ma'lumotlarni lug'ay ko'rinishida qaytaruvhi funksiya"""
    avto = {'kompaniya':kompaniya,
            'model':model,
           'rangi':rangi,
           'korobka':korobka,
            'yil':yili,
            'narhi':narhi}
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlar bit"""
    avtolar =[] #salondagi bosh avtolar uchun ro'yxat
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting:" , end=' ')
        kompaniya=input("Ishlab chiqaruvchi:>>")
        model = input("Modeli:>>")
        rangi=input("Rangi:>>")
        korobka=input("Korobka:>>")
        yili= input("Ishlab chiqarilogan yili:>>")
        narhi=input("Narhi:>>")