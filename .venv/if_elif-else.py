first=int(input('Введите 3 числа: '))
second=int(input())
third=int(input())
if first==second and first==third:
    print('Результат: 3')
elif first==second and first!=third or second==third and second!=first or first==third and first!=second:
    print('Результат: 2')
else:
    print('Результат: 0')