n = int(input("Введіть число n: "))
start = n if n % 2 == 0 else n - 1

for i in range(start, 0, -2):
    print(i, end=" ")
