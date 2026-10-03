def main():
    numbers = list(range(1, 11))
    n = int(float(input("Введите число: ").replace(",", ".")))

    if n in numbers:
        print(f"Число {n} найдено!")
    else:
        numbers += [n]
        print(f"Число {n} добавлено. Обновленный список: {numbers}")

if __name__ == '__main__':
    main()