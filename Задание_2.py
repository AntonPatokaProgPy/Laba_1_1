from math import log # Импортируем функцию log из библиотеки match

print("+ = Сложение \n""- = Вычитание \n" "* = Умножение\n""/ = Деление\n" "€ = Степень\n""# = Логарифмы\n""> = Округление  в большую\n""< = Округление  в меньшую\n""0 = Окончание сессии\n")
while True:
    s = input("Знак (+, -, *, /,€,>,<,#): ")
    if s == '0':
        break   # Выход из калькулятора(цикла) если s == 0
    if s in ('+', '-', '*', '/', '€', '>', "<", "#"):
        a = float(input("a = "))
        b = float(input("b = "))
        # "%.2f" - вывод строки формата число.00 Пример s = +, a = 3, b = 4 print("%.2f" % (a + b)) >>> 7.00
        if s == '+':
            print("%.2f" % (a + b))
        elif s == '-':
            print("%.2f" % (a - b))
        elif s == '*':
            print("%.2f" % (a * b))
        elif s == "€":
            print("%.2f" % (a ** b))
        elif s == '>':
            print(((a * 10 ** b // 1) + 1) / (10 ** b))
        elif s == '<':
            print(((a * 10 ** b // 1) / (10 ** b)))
        elif s == '#': # Функия log принимает 2 аргумента: числовое выражение,базовое занчение,если в функции не задано базовое значение,то log берется по основанию e.
            print(log(b, a))
        elif s == '/':
            if b != 0: # Проверка делимости на 0
                print("%.2f" % (a / b))
            else:
                print("Зачем делишь на 0?")
    else:
        print("Неверный значочек")
