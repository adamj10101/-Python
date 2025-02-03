#Напишите программу, которая выводит n строк треугольника Паскаля.
n = int(input("Введите количество строк треугольника Паскаля: "))
treug = []

for i in range(n):
    row = [1] * (i + 1)

    for j in range(1, i):
        row[j] = treug[i - 1][j - 1] + treug[i - 1][j]
    treug.append(row)

    print(' ' * (n - i - 1), end='')
    print(' '.join(map(str, row)))