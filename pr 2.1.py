#Напишите программу, в которой задается  натуральное число n и выводится обратная лестница из n ступенек.
# i-я ступенька должна состоять из чисел от 1 до i без пробелов.
for i in range(n, 0, -1):
    print(''.join(str(j) for j in range(1, i + 1)))
n = int(input("Введите натуральное число n: "))
for i in range(n, 0, -1):
    print(''.join(str(j) for j in range(1, i + 1)))