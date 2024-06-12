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
