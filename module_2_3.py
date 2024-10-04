my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index<len(my_list):
    vvod = int(input('Введите число из списка - 42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5: '))
    if vvod not in my_list:
        print('Вы ввели число не из списка!')
        continue
    elif vvod in my_list:
        print('Число положительное!')
        index += 1
        continue
    elif vvod<1:
        print('Вы ввели отрецательное число!')
    break


