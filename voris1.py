class Fan:
    def __init__(self, fan_nomi):
        self.fan_nomi = fan_nomi

class Talaba:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya
        self.fanlar = []

    def fanga_yozil(self, fan):
        self.fanlar.append(fan)

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
            print(f"{fan.fan_nomi} talabaning ro'yxatidan o'chirildi.")
        else:
            print("Siz bu fanga yozilmagansiz.")

# Test qilish uchun
talaba1 = Talaba("Ali", "Valiyev")
fan1 = Fan("Matematika")
fan2 = Fan("Informatika")
fan3 = Fan("Fizika")

talaba1.fanga_yozil(fan1)
talaba1.fanga_yozil(fan2)
talaba1.fanga_yozil(fan3)

talaba1.remove_fan(fan1)

print(f"{talaba1.ism}ning qolgan fanlari:")
for fan in talaba1.fanlar:
    print(fan.fan_nomi)


