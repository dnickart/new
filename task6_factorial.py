n = int(input("Введіть n для обчислення факторіалa: "))
factorial = 1

if n < 0:
    print("Факторіал не визначений для від'ємних чисел.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"!{n} = {factorial}")
