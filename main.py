"""import random
player = 1

while True:
    print("Ходит игрок " + str(player))
    input("Спустить курок? ")

    if random.randint(1,6) == 1:
        print("Выстрел")
        break
    else:
        print("Пусто")
    if player == 1:
        player = 2
    elif player == 2:
        player = 1
print("Вы проиграли")"""


"""a = int(input("Введите число "))
b = input("Введите знак ")
c = int(input("Введите число "))
if b == "+":
    print(a + c)
elif b == "-":
    print(a - c)
elif b == "*":
    print(a * c)
elif b == "/":
    try:
        print(a // c)
    except Exception as e:
        print(e)
        print("Ощибка на 0 делить нельзя")"""

"""try:
    a = int(input())
    print(a)
except Exception as e:
    print(e)"""

"Питон тутор урок 1"

"Есть список имен, написать функцию которая выбирает рандомное имя и возращает его" \
"условие в функцию передается список с именами"



"""import random

name = ["Паша" ,"Маша", "Миша","Коля"]
print(random.choices(name,k=3))
"""

"""import random

a = ["Паша", "Маша", "Миша", "Коля"]
def name(l):
    return random.choice(l)
print(name(a))
print(name([1,2,3,4]))"""


"""def sum(a,b):
   return a + b
print(sum(2,3))"""


"""i = 11
while i > 1:
    i = i - 1
    if i >= 5 and i <= 7:
        continue
    print(i)
"""

"""def f(a,b=0):
    return a - b
a = f(20,10)-f(7,4)
print(a)
"""


"""import requests
import csv
import time


info = []
o = 0
for с in range(1,101):

    url = "https://www.olx.kz/api/v1/offers/?offset="+str(o)+"&limit=50&category_id=112&filter_refiners=spell_checker&sl=18447c84abax3a8cf260"
    f = requests.get(url)
    a = f.json()
    try:
        data = a["data"]
    except:
        break

    for i in data:
        #print(i)
        title = i["title"]
        desc = i["description"]
        mesto = "Город: " +  i["location"]["city"]["name"] +  " / Область: " + i["location"]["region"]["name"]
        try:
            foto = i["photos"][0]["link"].replace(";s={width}x{height}", "")
        except:
            foto = "Нету"

        info.append([title,desc,mesto,foto])
    o = o + 50
    print(с,"% Спаршено" )
    if с % 10 == 0:
        print("Задержка 60 сек. Защита от блокировки.")
        time.sleep(60)


print("Запись в файл")
file = open("Спаршено.csv","w",encoding='utf-8')
file_writer = csv.writer(file, delimiter="\t")
for i in info:
    file_writer.writerow(i)


#file_writer.writerows(info)
"""



"""class Car:
    def __init__(self,marca,color,hozain="Нет хозяина"):
        self.marca = marca
        self.color = color
        self.hozain = hozain
        self.cena=1000

    def info(self):
        print("Марка:",self.marca)
        print("Цвет:",self.color)
        print("Стоимость:",self.cena)
        print("Хозяин:",self.hozain)

    def izmenit_cenu(self,cena):
        self.cena = cena
        #print("Цена успешно изменена")

    def izmenit_hozaina(self,hozain="Нет хозяина"):
        self.hozain = hozain
        print("Хозяин успешно изменен на:",self.hozain)


car1 = Car("Форд","Красный","Джеймс")
car2 = Car("Мерсижес","Черный","Джесика")
car2.izmenit_cenu(cena=5000)"""


"""class Vector3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def Koord(self):
        print(self.x,self.y,self.z)

    def __str__(self):
        return str(self.x) + " " +   str(self.y)  + " " + str(self.z)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector3D(x,y,z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector3D(x, y, z)
    def norm(self):
        rez = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        return rez

Vec1 = Vector3D(4,1,2)
Vec2 = Vector3D(3,5,8)
Vec3 = Vec1 - Vec2
print(Vec3)
print(Vec2.norm())"""



"""Класс «Прямоугольный треугольник»
Класс содержит два действительных числа – стороны треугольника. и включает
следующие методы:
− увеличение/уменьшение размера стороны на заданное количество процентов;
− вычисление радиуса описанной окружности,
− вычисление периметра,
− определение значений углов. """



"""class rectangle():
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length
        self.height = (self.breadth ** 2 + self.length ** 2) ** 0.5

    def umnojit(self):
        return self.breadth * self.length * self.height


    def minus(self):
        return self.breadth - self.length


    def pribavit(self):
        return self.breadth + self.length

    def pirimetr(self):
        return self.breadth + self.length + self.height

a = int(input("Введите длину прямоугольника: "))
b = int(input("Введите ширину прямоугольника: "))

obj = rectangle(a, b)
print("Радиус описанной окружности:", obj.umnojit())


print("Уменьшения размера сторон:", obj.minus())


print("Увеличение размера сторон:", obj.pribavit())


print("Периметр треугольника:", obj.pribavit())"""



'''class Ofis:
    def __init__(self,mesto,razmer):
        self.mesto = mesto
        self.razmer = razmer
        self.zanato = 0
        self.info()


    def info(self):
        print("Количество мест:",self.mesto)
        print("Количество м2:",self.razmer)
        print("Количество занятых мест:",self.zanato)
        print()

    def zanatomest(self,mesta):
        if mesta > self.mesto:
            print("Ошибка: не достаточно мест")
            return
        self.zanato = mesta
        print("Новое значение установленно:", self.zanato)'''



"""class Celovek:
    def __init__(self,name,ln,age=1,sex="М"):
        self.name = name
        self.lastname = ln
        self.age = age
        self.sex = sex
        self.kids = []
        self.partner = "Нет"

    def info(self):
        print("---------------Информация----------------")
        print("Имя:",self.name)
        print("Фамилия:", self.lastname)
        print("Возраст:",self.age)
        print("Пол:", self.sex)
        print("Дети:", self.kids)
        print("Партнер:", self.partner)

    def svadba(self,partner):
        self.partner = partner
        partner.partner = self
        print("Свадьба сыграна")


    def __str__(self):
        return self.name + " " + self.lastname

cel1 = Celovek("Иван","Петров",27)
devuska = Celovek("Мария","Зайцева",20,"Ж")
cel1.svadba(devuska)
cel1.info()
devuska.info()
print(cel1)"""



"""class Cat:
    def __init__(self,klicka,okras,old,poroda):
        self.klicka = klicka
        self.okras = okras
        self.old = old
        self.poroda = poroda


    def info(self):
        print("Кличка:",self.klicka)
        print("Окраска:",self.okras)
        print("Года:",self.old)
        print("Порода:",self.poroda)




cat = Cat("Барсик","Полосатый",2,"Голубая русская кошка")
cat1 = Cat("Гучи","Пятнистый",3,"Бенгальская")
cat.info()
print()
cat1.info()"""


 






