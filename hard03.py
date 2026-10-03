import random

def main():
    secret_num = random.randint(1, 10)
    n = int(float(input("Введите число от 1 до 10: ").replace(",", ".")))

    if (n >= 1) and (n <= 10):
        if n == secret_num:
            print("Угадали!")
        elif n > secret_num:
            print("Загаданное число меньше.")
        else:
            print("Загаданное число больше.")
    else:
        print("Ваше число меньше 1 или больше 10")

if __name__ == '__main__':
    main()