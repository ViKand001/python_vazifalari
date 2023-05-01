# -*- coding: utf-8 -*-
"""
Created on Mon May  1 15:00:33 2023

@author: Kamalov M
"""

#20 dars : Funksiyadan qiymat qaytarish


#def toliq_ism_yasa(ism, familiya):
#    """Toliq ism qaytaruvchi dastur"""
#    toliq_ism = f"{ism} {familiya}"
#    print(toliq_ism) 
#    
#toliq_ism_yasa('Utkir', 'Aytimbetov')    


#def toliq_ism_yasa(ism, familiya):
#    """Toliq ism qaytaruvchi dastur"""
#    toliq_ism = f"{ism} {familiya}"
#    return (toliq_ism) 
#    
#talaba1 = toliq_ism_yasa('Samandar', 'Orazbayev') 
#talaba2 = toliq_ism_yasa('Sunnat' ,'Aliqulov')
#print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
#print(f"{talaba1} darsga kechikib keldi!")   


#def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#   """Toliq ism qaytaruvchi dastur"""
#    if otasining_ismi:
#        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#   else:
#       toliq_ism = f"{ism} {familiya}"
 #       return toliq_ism.title()
#   
#talaba1 = toliq_ism_yasa('Sodiq', 'Po\'latov ' )
#talaba2 = toliq_ism_yasa('Begzot', 'Gulomjanov', 'Olimovich')
#print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")  
    




def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rangi':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto
avto1 = avto_info('GM', 'Malibu','Qora', 'Avtomat', '2018')
avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016,15000)
avtolar = [avto1, avto2]
print('Onlayn bozordagi mavjud avto mashinalar:')
for avto in avtolar:
    if  avto['narh']:
         narh = avto['narh']
    else:
         narh = "Nama'lum"
    print(f"{avto['rangi']} {avto['model']}. Narhi : {narh}")     
    