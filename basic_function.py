# python3

print('Определите необходимую операцию: ')
print('"сложение" или "+" -- суммирует значение первого и второго числа;')
print('"вычитание" или "-" -- вычитает второе значение из первого;')
print('"умножение" или "*" -- умножает первое значение на второе;')
print('"деление" или "/" -- делит первое значение на второе;')
print('"степень" или "^" -- возводит первое значение в степень второго значения.')
name_function = input('Введите название операции: ')
print('Введите два аргумента.')
first_argument = float(input('Введите первое число: '))
second_argument = float(input('Введите второе число: '))

if name_function == 'сложение' or name_function == '+':
    print('Сумма значений {} и {}: '.format(first_argument, second_argument), first_argument + second_argument)
elif name_function == 'вычитание' or name_function == '-':
    print('Разность значений {} и {}: '.format(first_argument, second_argument), first_argument - second_argument)
elif name_function == 'умножение' or name_function == '*':
    print('Произведение значений {} и {}: '.format(first_argument, second_argument), first_argument * second_argument)
elif name_function == 'деление' or name_function == '/':
    print('Результат деления {} на {}: '.format(first_argument, second_argument), first_argument / second_argument)
elif name_function == 'степень' or name_function == '^':
    print('Степень {} числа {}: '.format(second_argument, first_argument), first_argument ** second_argument)
else:
    print('Вы ввели неверное значение функции.')
