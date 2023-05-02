# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:22:00 2023

@author: Kamalov M
"""

#19:55 02.05.2023 Funksiyaga ro'yxat uzatish'
def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()} ning bahosi:>>")
        baholar[ism]=int(baho)
    return baholar

talabalar  =['Ali', 'Utkir', 'Oybek', 'Sodiq']
baholar = bahola(talabalar[:])
print(baholar)
   