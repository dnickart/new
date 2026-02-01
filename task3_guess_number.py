import random

target = random.randint(1, 10)
attempts = 3

print("Я загадав число від 1 до 10. У тебе 3 спроби!")

for i in range(attempts):
    guess = int(input(f"Спроба {i+1}. Твій варіант: "))
    if guess == target:
        print("Вітаю! Ти вгадав!")
        break
    elif guess < target:
        print("Більше")
    else:
        print("Менше")
else:
    print(f"На жаль, спроби закінчилися. Я загадав {target}.")
