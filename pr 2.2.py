#Напишите программу, в которой задается натуральное число n и выводится перевернутая пирамида из n ступенек, i-я ступень должна состоять из чисел от 1 до i и обратно без пробелов
n = int(input("Введите натуральное число n: "))

for i in range(n, 0, -1):
    left = ""
    right = ""

    for j in range(i, 0, -1):
        left += str(j)

    for j in range(2, i + 1):
        right += str(j)

    row = left + right

    s = " " * (n - i)
    print(s + row)
