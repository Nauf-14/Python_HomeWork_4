#  В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод —
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль,находясь перед некоторым кустом заданной во входном файле грядки.

# import random

# numb_sets = int(input("Введите кол-во кустов черники: "))
# data = [random.randint(1, 10) for _ in range(numb_sets)]
# print(f"Начальный массив: {data}")

# big_summ = 0
# for i in range(1, len(data) - 1):
#     current_summ = data[i - 1] + data[i] + data[i + 1]
#     if current_summ > big_summ:
#         big_summ = current_summ

# if data[-1] + data[-2] + data[0] > big_summ:
#     big_summ = data[-1] + data[-2] + data[0]

# if data[-1] + data[0] + data[1] > big_summ:
#     big_summ = data[-1] + data[0] + data[1]

# print(big_summ)

import random

numb_sets = int(input("Введите кол-во элементов массива: "))
data = [random.randint(1, 10) for _ in range(numb_sets)]
print(f"Начальный массив: {data}")

big_summ = 0
for i in range(len(data)):
    current_summ = data[i-1] + data[i] + data[(i+1)%len(data)]
    if current_summ > big_summ:
        big_summ = current_summ

print(big_summ)









