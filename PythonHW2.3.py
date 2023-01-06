# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

print('Введите число')
N = int(input())
sum_nums = 0
list_nums = []

for i in range(1, N + 1):
    result = round((1 + 1 / i) ** i, 3)
    list_nums.append(result)
    sum_nums += result

print(f'Список чисел {list_nums}')
print(f'Сумма чисел {sum_nums}')
# Программа работает