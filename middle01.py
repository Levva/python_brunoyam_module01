number = int(float(input("Введите число: ").replace(",", ".")))

if number > 0:
    print("Число положительное.")
elif number < 0:
    print("Число отрицательное.")
else:
    print("Это ноль.")