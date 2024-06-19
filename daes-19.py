def summa(*sonlar):
    """Kiritilgan sonlar ko'paytmasini hisoblaydigan funksiya"""
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma
print(summa(1,2))
print(summa(1,3,4))


def talaba_info(ism, familiya, **kwargs):
    kwargs['ism']=ism
    kwargs['familiya']=familiya
    return kwargs

talaba = talaba_info('zilola', 'iskandarova',yoshi = '15', t_joyi = 'Xorazm')
print(talaba)
