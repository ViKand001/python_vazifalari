#10-dars Tarmoqlash
#Muallif JOodasov Asilbek

#avtolar = ['Audo', 'bmw', 'volvo', 'kia', 'hyundai']
#for avto in avtolar:
#      if avto == 'bmw':
#           print(avto.upper())
#      else:
#           print(avto.title())
           
#ism = 'Ali'
#ism.lower() == 'Ali' 

#ism = input('Ismingiz nima?\n>>>')
#if ism.lower() != 'ali' :
  #  print(F"Uzr, {ism.title()} biz Alini kutyabmiz.")
#else:
 #    print('Salom, Ali ')   
 

#javob = float(input("12x6 nechiga teng>>>"))
#if javob != 72:
 #   print("javob xato!")
 
 
#yosh = int(input("Yoshingiz nechida?>>>"))
#if yosh>=18:
 #   print('Xush kelibsiz bizning safimizga')
#else:
  #  print("Siz hali yoshsiz, sizga kirish mumkin emas!")
    
    
#login = input("Yangi login yarating:")
#if len(login)<=5:
 #   print("Login 5 harfdan ko'proq bo'lishi shart")   
    
#yil = int(input("Tug'ilgan yilingizni kiriting>>>"))
#if 2020-yil<18:
 #   print(f"Yoshingiz {2020-yil}da ekan.")
  #  print("Kirish mumkin emas!")
#else:
 #   print("Bizning safimizga hush kelibsiz.")    
 

#yosh = int(input("yoshingiz nechida?>>>"))
#if yosh>65: print("siz Covid-19 risk guruhida ekansiz!")

#x, y, = 252, 50
#print("x>y") if x>y else print("x<y")

# 11-dars boshlandi:17:28 25.04.2023

#son = -50
#if son<0:
 #   print("Manfiy son")
#else:
 #   print("Musbat son")
 
#yosh = int(input("Yoshingiz nechida>>>"))
#if yosh<=4:
#    print("sizga kirish mutlaqo bepul")
#elif yosh<=12:
#   print("sizga kirish 5000 so'm")
#elif yosh<=16:
 #   print("Sizga kirish 8000 so'm")
#else:
 #   print("Sizga kirish 10000 so'm")
 
#yosh = int(input("Yoshingiz nechida>>>"))
#if yosh<=4:
 #     narh = 0
#elif yosh<=12:
 #     narh = 5000
#elif yosh<=16:
 #     narh = 8000
#else:
 #     narh = 10000
      
#print(f"Sizga kirish {narh} so'm")

#kun = input("Bugun nima kun?>>>")
#if kun.lower() =='shanba' or kun.lower() == 'yakshanba':
 #    print('Bugun dam olish kuni.')
#else:
 #    print("bugun ish kunim ekan.") 


#kun = input("Bugun nima kun>>>")
#harorat = float(input('Havo harorati qanday>>'))

#if kun.lower()=="yakshanba" or kun.lower()=='shanba' and harorat>=30:
  #  print("Cho'milgani ketdik")
#elif kun.lower()=="yakshanba"or kun.lower()=='shanba' and harorat<30:
 #    print("Uyda dam olamiz!")    
 
    
#narh = 15000
#choy = True
#salat = True
#if choy and salat:
 #   narh = narh + 10000
#elif choy or salat:
 #   narh = narh + 5000

#print(f"Jami {narh} so'm")   
 
    
#narh = 15000
#choy = 1
#salat = 0
#non = 0
#kompot =1
#assorti =1
 
#if choy:
 #   print("Mijoz choy oldi.")
  #  narh = narh + 3000
     
#if salat:
 #   print("Mijoz salat oldi.")
  #  narh = narh + 5000
    
#if non:
 #  print("Mijoz non sotib oldi.")
  # narh = narh + 2000
   
#if kompot:
 #  print("Mijoz kompot sotib oldi.")
  # narh = narh + 5000 
   
#if assorti:
 #  print("Mijoz assorti sotib oldi.")
  # narh = narh + 15000
   
#print(f"Jami bo'lib {narh} so'm")
    
    
#menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
#'manti' in menu

#menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
#ovqat = input("Nima ovqat yeysiz?>>>")
#if ovqat.lower()  in menu:
 #   print("buyurtma qabul qilindi.")
#else:
 #  print("Afsuski bizda bunday ovqat yo'q.")
    

 
#menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
#buyurtmalar = ["osh", "somsa", "manti",  "shashlik",]
#if buyurtmalar:
 #   for taom in buyurtmalar:
 #       if taom in  menu:
  #             print(f"Menuda {taom} bor")
   #     else:
   #            print(f"Kechirasiz, ,menuda {taom} yo'q") 
#else:
 #   print("Savatchangiz bo'sh")
 
 # 12-dars XAtolar bilan ishlash
 
 
 
 # 15-dars Dictionary
 #26.04.2023
 
#car_0 = {'model' : 'Gentra', 'rangi' : 'qora'}
#print(car_0['model'])
#print(car_0['rangi'])
 
#en_uz = {'apple' : 'olma', 'apricot' : 'o\'rik', 'banana' : 'banan' }

#mevalar = {"olma" : 10000, 'tarvuz' : 8000, 'qovun' :10000}
#print(f" Olma narhi {mevalar['olma']} so'm")

# Lug'atda istalgan  ma'lumot turlarini saqlash.
#talaba_0 = {"ism":"Murod Olimov", "yosh":20, "t_yil":2000}
#print(f"{talaba_0['ism'].title()},\
 #    {talaba_0['t_yil']}-yilda tugilgan,\
  #     {talaba_0['yosh']} yoshda ")      
          
# Yangi kalit qo'shish
#talaba_0['kurs'] = 4
#talaba_0['fakultet'] = 'informatika'
# o'zgartirish
#talaba_0['ism'] = 'Asilbek'

# Bo'sh lug'at
#talaba_1 = {}
#talaba_1['ism'] = 'Joldasov Asilbek'
#talaba_1['kurs'] = 2
#talaba_1['yosh'] = 20
#print(talaba_1)

#Qiymatni yangilash
#talaba_1['kurs'] = 3

# Kalit so'z qiymayni ochirin tashlash
#talaba_1 = {'sim': 'joldasov asilbek', 'yosh':20 }
#del talaba_1['yosh']

telefonlar = {
   'ali':'galaxy s9',
   'vali': 'Samsung 10S',
   'olim': 'mi 10 pro',
   'orif':'nokia 3310'
    }


#get metodi
phone = telefonlar['ali']
print(f"alining telefoni{phone}")

phone = telefonlar
print(phone)


# 19:34  01.05.2023














































 
 
 