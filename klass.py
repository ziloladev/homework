class Student:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.sinf = 9

    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.sinf}-sinf "

student1 = Student("Zilola", "Iskandarova", 2009)
print(student1.get_info())

# class Student:
#
#     def __init__(self, ism, familiya, tyil, email):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.email = email
#
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.email} "
#
#     def set_bosqich(self, email):
#         self.gmail = email
#
# talaba1 = Student("Alijon","Valiyev",2000, "iskandarovazilola696@gmail.com")
# print(talaba1.get_info())
#


