def greet(name):
    return f"Привет, {name}! Рад тебя видеть!"

def main():
    name = ""
while True:
    name = input("Введите имя (или q для выхода): ")
    if name == "q":
        break
    print(greet(name))   

if __name__ == '__main__':
    main()