dlar = {
    'AQSH': 'Washington',
    'ITALIYA':'Rim',
    'ROSSIYA':'Moskva',
    'TOJIKISTON':'Dushanbe',
    "QOZOG'ISTON":'Nursulton',
    'MALAYZIYA':'Kuala-Lumpur',
    "O'ZBEKISTON":'Toshkent',
    "QIRG'IZISTON":'Bishkek',
    'SINGAPUR':'Sungapur'
}
print("Dunyo davlatlari:")
for h1 in sorted(dlar.keys()):
    print(h1)
print("Davlatlarning poytaxtlari:")
for h2 in sorted(dlar.values()):
    print(h2)

dlar = {
    'AQSH': 'Washington',
    'ITALIYA':'Rim',
    'ROSSIYA':'Moskva',
    'TOJIKISTON':'Dushanbe',
    "QOZOG'ISTON":'Nursulton',
    'MALAYZIYA':'Kuala-Lumpur',
    "O'ZBEKISTON":'Toshkent',
    "QIRG'IZISTON":'Bishkek',
    'SINGAPUR':'Sungapur'
}
soz = input("Istalgan davlatingizni kiriting: ")
if soz in dlar:
    print(f"{soz} ning poytaxti: {dlar[soz]}")
else:
    print("Bizda bunday davlat mavjud emas")

