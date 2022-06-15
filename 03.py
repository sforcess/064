# # !!!
#
# def fun(a):
#     print(a)
##
# a = 10
# print(fun(a))
#
#
#
# # res = fun(a)
# # print(res)

class Emploee:
    # name = 'None'
    # surname = 'None'

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def say_hello(self):
        print(f'{self.name} {self.surname} says Hello!!!')

e1 = Emploee('Ivan', 'Ivanov')
# print(e1.name)
# print(e1.surname)
# e1.name = 'Ivan'
# e1.surname = 'Ivanov'
e1.say_hello()

e2 = Emploee()
print(e2.name)
print(e2.surname)