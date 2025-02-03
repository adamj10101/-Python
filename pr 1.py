#Напишите программу, которая принимает 3 числа, сравнивает между собой и возвращает максимальное и минимальное числа.
#Программа должна также корректно обрабатывать различные варианты равенств чисел. Функции min и мах не использовать
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
c = int(input("Введите третье число:"))

maximum = None
minimum = None

#для макс
if a >= b:
    if a >= c:
        maximum = a
    else:
        maximum = c
else:
    if b >= c:
        maximum = b
    else:
        maximum = c

#для мин
if a <= b:
    if a <= c:
        minimum = a
    else:
        minimum = c
else:
    if b <= c:
        minimum = b
    else:
        minimum = c

if a == b and b == c:
    print("все чилса одинаковые")
else:
    print(f"Максимальное число: {maximum}")
    print(f"Минимальное число: {minimum}")




