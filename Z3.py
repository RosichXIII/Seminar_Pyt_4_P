# 32). Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import random
numbers_sequence = []
for i in range(random.randint(3, 30)):
    numbers_sequence.append(random.randint(0, 25))
print('Последовательность:', numbers_sequence)
unique_numbers_sequence = []
for i in numbers_sequence:
    if i in unique_numbers_sequence:
        continue
    else:
        unique_numbers_sequence.append(i)
print('Последовательность уникальных знеачений:',unique_numbers_sequence)