# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 19:51:13 2023

JOldasov Asilbek"""

#17-dars

#son = 1 # songa 1 qiymat beramiz
#while son<=5: # toki son 5ga kichik yoki teng ekan
 #   print(son, end=' ') # sonni konsolga chiqaramiz.
 #   #son = son + 1 # songa birni qo'shamiz
  #  son += 1
#print("Dastur tugadi")  

# while va input  
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan sonni kiriting"
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): deb yozing"
#qiymat = ''
#while qiymat !='exit':
#    qiymat = input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)
#print("dastur tugadi")

# ishora
#print("kiritilgan sonning kvadratini qauytaruvchi dastur.")
#savol = "Istalgan sonni kiriting"
#savol +="(Dasturni to'xtatish uchun 'exit' deb yozing): "
#ishora = True
#while ishora:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        ishora = False
#    else:
#       print(float(qiymat)**2)  
#rint("Dastur to'xtadi")        



# break while
#print("kiritilgan sonning kvadratini qauytaruvchi dastur.")
#savol = "Istalgan sonni kiriting"
#savol +="(Dasturni to'xtatish uchun 'exit' deb yozing): "

#while True:  # abadiy sikl
#    qiymat = input(savol)
 #   if qiymat == 'exit':
#        break # tsikl to'xtatish
#    else:
#       print(float(qiymat)**2)  
#print("Dastur to'xtadi")     


# break for
#sonlar = list(range(1,11)) 
#for son in sonlar:
#    if son ==5:
#        break
#    print(f"{son} ning kvadrati {son**2} ga teng")
 

# Continue


#sonlar = list(range(1,11))
#for son in sonlar:
#     if son==5:
#         continue
#     print(f"{son}ning kvadrati {son**2} ga teng")



#Continue while
son = 0
while son<=10:
    son += 1
    if son%2!== 0:
        continue
    else:
        print(son)
        
   