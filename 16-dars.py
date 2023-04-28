# -*- coding: utf-8 -*-

#Created on Thu Apr 27 19:27:43 2023

#15-dars Lug'atlar bilan ishlash
#talaba_0 = {
 #   'ism':'oybek',
  #  'familiya': 'Norboyev',
   # 'yosh': 22,
    #'fakultet ' : 'matematika',
     #'kurs': 2
   #  }

#print(talaba_0.items())

#for kalit, qiymat in talaba_0.items():
 #   print(f"kalit: {kalit}")
  #  print(f"Qiymat: {qiymat} \n")
  
#telefonlar = {
#    'ali': 'Iphone X',
#    'vali': 'galaxy s9',
#    'olim': 'mi 10 pro',
#    'orif': 'Nokia 3310',
#    'Oybek': 'Redmi 11 pro',
#    'Ergashev.D': 'Iphone X',
#    'Dilshod': 'Nokia 3310'
#   }  
#for k, q in telefonlar.items():
 #   print(f"{k.title()}()ning telefoni {q}")
 
# keys()
#mahsulotlar = {
#    'olma': 10000,
#    'anor': 12000,
#   'uzum':15000,
#   'anjir': 20000,
#   'shaftoli': 15000,
#    } 
#print(mahsulotlar.keys())

#print('Dokondagi mavjud mahsulotlar:')
#for mahsulot in mahsulotlar.keys():
#        print(mahsulot.title())
        
        
#bozorlik = ['anor', 'limon', 'uzum', ' non', 'baliq ikra']
#for mahsulot in mahsulotlar:
#    if mahsulot in bozorlik:
#        print(f"{mahsulot.title()} { mahsulotlar[mahsulot]} so'm")
#        
#for buyum in bozorlik:
#    if buyum not in mahsulotlar:
#        print(buyum)  
#        print(f"Iltimos, do'koningizga {buyum} ham olib kleing!")
          
        
#print("Do'konimizdagi mahsulotlar:")
#for mahsulot in sorted(mahsulotlar):
#         print(mahsulot.title())     
         
#print(telefonlar.values())

#for tel in telefonlar.values():
#    print(tel)
#
#print("foydalanuvchi quyidagi telefonlardan birini ishlatishadi:")
#for tel in set(telefonlar.values()):
#    print(tel)
      

#toys = {"ball", "car", "horse", "lamp", "ball", "bear", "horse"}


 


#28.04.2023 17:43
# 16-dars: Nesting
 

car0 = {
        'model': 'lacetti',
        'rangi': 'oq',
        'yil': 2018,
        'narh': 13000,
        'km': 50000,
        'korobka': 'avtomat'
        }
car1 = {
        'model': 'nexia-3',
        'rangi': 'qora',
        'yil': 2015,
        'narh': 90000,
        'km': 89000,
        'korobka': 'mexanika'
        }  
car2 = {
        'model': 'gentra',
        'rangi': 'qizil',
        'yil': 2019,
        'narh': 15000,
        'km': 20000,
        'korobka': 'mexanika'
        }
#car = car0
#print(f"{car['model'].title()}, "
#      f"{car['rangi']} rangi, "
#      f"{car['yil']}-yil, {car['narh']}$")
#
#ar = car1
#print(f"{car['model'].title()}, "
#      f"{car['rangi']} rangi, "
#      f"{car['yil']}-yil, {car['narh']}$")

#car = car2
#print(f"{car['model'].title()}, "
#      f"{car['rangi']} rangi, "
#      f"{car['yil']}-yil, {car['narh']}$")


#cars = [ car0, car1,car2]
#for car in cars:
#    print(f"{car['model'].title()}, "
#          f"{car['rangi']} rangi,"
#          f"{car['yil']}-yil, {car['narh']}$")
    

malibus = []
for yangi in range(10):
    new_car = {
        'model': "Malibu",
        'rangi': None,
        'yil': 2023,
        'narh': None,
        'km': 0,
        'korobka': 'avto'
        }
    malibus.append(new_car)
  
    
#for malibu in malibus[:3]:
#    malibu['rangi']='qizil'
#    print(malibu)  
    
    
#for malibu in malibus[3:6]:
#    malibu['rangi']='Qora'
#   print(malibu)


#for malibu in malibus[6:10]:
#    malibu ['rangi']= 'ko\'k'
#    malibu ['korobka']= 'mexanik'
#   print(malibu)
#    
#for malibu in malibus:
#    if malibu['korobka']=='avto':
#        malibu['narh']=40000
#   else:
#      malibu['narh']=35000
#for malibu in malibus:
#    print(malibu)        


# Lug'at ichida ro'yxat
dasturchilar = {
    'ali':['python', 'c++'],
    'vali':  ['html',  'css', 'js',],
    'hasan':['php', 'sql'],
    'husan': ['python', 'php'],
    'maryam': ['c++', 'c#']
    }


#for ism, tillar in dasturchilar.items():
 #   print(f"\n{ism.title()}  quyidagi dasturlash tillarini biladi:")
  #  for til in tillar:
   #     print(til.upper())


#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()}  quyidagi dasturlash tillarini biladi:")
#   for til in tillar:
#        print(f'{til.upper()} ' , end='')


hamkasblar = {
    'ali': {'familiya': 'valiyev',
            't_yil': 1995,
            'malumoti': 'oliy',
            'tillar': ['python', 'c+++']
            },
    'vali': {'familiya': 'aliyev',
             't_yil': 2001,
             'malumoti': 'o\'rta maxsus',
             'tillar': ['html', 'css', 'js']
             },
    'hasan': {'familiya': 'husanov',
              't_yil': 1999,
              'malumoti': 'maxsus',
              'tillar':['python', 'php']}    
        }
for ism, info in hamkasblar.items():
        print(f"\n{ism.title()} {info['familiya'].title()},"
              f"{info['t_yil']}-yilda tu'gilgan."
              f"malumoti : {info['malumoti']}. \n"
              "Quyidagi dasturlash tillarini biladi:")
        for til in info['tillar']:
            print(til.upper())


























         
        