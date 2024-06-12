# son = 1
# while son<=5:
#     print(son, end='')
# #     son = son + 1
# print("Kiritilgan sonnning kvadratini qaytaruvchi dastur")
# savol = "Istalgan sonni kiriting"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# sonlar = list(range(1,10))
# for son in sonlar:
#     if son == 11:
#         break
#     print(f"{son} ning kvadrati {son**2} ga ten
# ismlar = []
#
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)  # ism kalit, yosh qiymat
#
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/no)")
#     if javob == "no":
#         ishora = False
#
# for ism, yosh in dostlar.items():
# #     print(f"{ism.title()} {yosh} yoshda")
# cars = ['lacetti', 'nexia', 'toyota', ' nexia', 'audi', 'malibu', 'nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)
# talabalar = ['zilola', 'shahnoza', 'gullola', 'hilola']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho
#
#
# print(baholangan_talabalar)
#
# print('Buyurtma qabul qiluvchi dastur!')
# savol='Iltimos,buyurtma bering!'
# savol+="(dasturni yo'qotish uchun 'end' deb yozing): "
# buyurtma=''
# while buyurtma !='end':
#     buyurtma=input(savol)
#     if buyurtma !='end':
#         print(buyurtma)
# buyurtmalar = ['o\'rik','anjir','anor','olma']
# mahsulotlar = {
#                "o'rik":20000,
#                'anjir':25000,
#                'anor':18000,
#                'olma':22000
# }
# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} - {narh} so'm")

