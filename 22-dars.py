# -*- coding: utf-8 -*-
"""
Created on Tue May  2 15:10:11 2023

@author: Kamalov M
"""
#20:22 02.05.2023
#*args va **kwargs keywords


#def summa(*sonlar):
#    """ Kiritilgan sonlarning yig'insini hisoblaydigan funksiya"""
#    yigindi = 0
#    for son in sonlar:
#        yigindi += son
#    return yigindi

#print(summa(1,2))
#print(summa(1,2,3,4,5))
#print(summa(4,5,6,7))

#def summa(*sonlar):
#    """ Kiritilgan sonlarning yig'insini hisoblaydigan funksiya"""
#    return sum(sonlar)

#print(summa(2))
#print(summa(1,2,3,4,5))
#print(summa(4,5,6,7))   

#def summa(x,y, *sonlar):
#    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#    return x+y+sum(sonlar)
#
#print(summa(1,2))
#print(summa(1,2,3,4,5))
#print(summa(4,5,6,7))

def avto_info(kompaniya, model, **malumotlar):
    """Avto haqida ma'lumotlarni lug'at ko'rinishida qaytyaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return  malumotlar

avto1 = avto_info("GM", "Malibu", rangi='qora', yil=2019)
avto2 = avto_info("Kia", "K5", rangi='oq', narh = 35000, yil=2022, korobka='avtomat')
