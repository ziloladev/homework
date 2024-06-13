cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != 'gm':
        print(car.upper())
    else:
        print(car.title())

ism = input('Ismingiz nima?\n')
if ism.lower() == 'admin':
   print(f"Xush kelibsiz, Admin")
   print("Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
   print(f"Xush kelibsiz, {ism}")


sonlar = int(input('Istalgan sonni kiriting:'))
if sonlar > 0:
    print('Musbat son')
elif sonlar < 0:
    print("Manfiy son")


sonlar = int(input('Istalgan sonni kiriting:'))
if sonlar > 0:
    print(f"{sonlar**2} ")
elif sonlar < 0:
    print("Musbat son kiriting!")

yosh = int(input('Yoshingiz nechida?'))
if yosh<=4:
    price = 0
elif yosh>=60:
    price = 0
elif yosh<=18:
    price = 10000
else:
    price = 20000

print(f"Sizga kirish {price} so'm")
