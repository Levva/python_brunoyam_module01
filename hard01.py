def convert_temp(temp, unit):
    if unit in "Ff":
        return (temp - 32) * 5 / 9
    elif unit in "Cc":
        return (temp * 9 / 5 ) + 32
    else: return "Неизвестная система измерения"

def main():
    temp = input("Введите температуру (градусы и систему измерения C или F): ")
    unit = temp[-1]
    temp = int(temp[:-1])
    result =  convert_temp(temp, unit)
    print(result)

if __name__ == '__main__':
    main()