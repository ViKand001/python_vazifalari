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
            'narhi':narhi}
    return avto

print("saytimiz avtolar ro'yxatinin shakllantiramiz.")
avtolar =[] #salondagi bosh avtolar uchun ro'yxat
while True:
    print("\n Quyidagi ma'lumotlarni kiriting:" , end=' ')
    kompaniya=input("\nIsHlab chiqaruvchi:>>")
    model = input("Modeli:>>")
    rangi=input("Rangi:>>")
    korobka=input("Korobka:>>")
    yili= input("Ishlab chiqarilogan yili:>>")
    narhi=input("Narhi:>>")
    #foydalanuvchi kiritgan ma'lumotlardan avto_info yordamida
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz.
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    # Yana avtomashina qo'shasizmi?
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob == "no" :
        break

print("\n Salonimizdagi avtolar:")
for avto in avtolar:
    if avto['narhi']:
        narhi = avto['narhi']
    else:
        narhi = "Na'malum"
    print(f"{avto['rangi'].title()} {avto['model'].title()}, {korobka} korobka. Narhi : {narhi}")    

#avto1 = avto_info('GM', 'Malibu','Qora', 'Avtomat', '2018')
#avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016,15000)
#avtolar = [avto1, avto2]
#rint('Onlayn bozordagi mavjud avto mashinalar:')
#or avto in avtolar:
#   if  avto['narh']:
#         narh = avto['narh']
#    else:
#        narh = "Nama'lum"
#    print(f"{avto['rangi']} {avto['model']}. Narhi : {narh}")     
 

#def oraliq(min,max, qadam):
 #   sonlar = []
 #   while min<max:
 #       sonlar.append(min)
 #       min += 1
#    return sonlar
#print(oraliq(0,10))
#print(oraliq(10,21))
    
        