
 s_taomlar = {
    't1':'kabob',
    't2':'osh',
    't3':'manti',
    't4':'somsa',
    't5':'barak'
}
taomlar = s_taomlar['t1']
print(f'Otamning sevimli taomi {taomlar}')
taomlar = s_taomlar['t4']
print(f'Onamning sevimli taomi {taomlar}')
taomlar = s_taomlar['t5']
print(f'Ukamning sevimli taomi {taomlar}')
taomlar = s_taomlar['t3']
print(f'Opamning sevimli taomi {taomlar}')

ing_lugat = {
    'print':'chop etish',
    'if': 'agar',
    'else': 'boshqa',
    'input':'kirish',
    'integer':'butun son',
    'float':'xaqiqiy son',
    'elif':'agar',
    'string':'aralashtriish',
    'list':'royxat',
    'for':'uchun'
}
lugat = ing_lugat['print']
print(f' print-{lugat}')
lugat = ing_lugat['input']
print(f' input-{lugat}')
lugat = ing_lugat['elif']
print(f" elif-{lugat}")
lugat = ing_lugat['for']
print(f' for-{lugat}')
lugat = ing_lugat['integer']
print(f' integer-{lugat}')
lugat = ing_lugat['else']
print(f' else-{lugat}')
lugat = ing_lugat['float']
print(f' float-{lugat}')
lugat = ing_lugat['if']
print(f' if-{lugat}')
lugat = ing_lugat['list']
print(f' list-{lugat}')
lugat = ing_lugat['string']
print(f' string-{lugat}')


python_lugat = {
    'integer': 'butun son',
    'float': "o'nli son",
    'string': 'matnli qatorda',
    'if': 'agar',
    'else': 'aks holda',
    'list': "ro'yxat",
    'tuple': "o'zgarmas ro'yxat",
    'dictionary': "lug'at",
    'for': 'uchun',
    'while': 'davomida'
}
soz = input("Biror so'z kiriting: ")
if soz in python_lugat:
    print(f"{soz} so'zining tarjimasi: {python_lugat[soz]}")
else:
    print("Bunda so'z mavjud emas")


