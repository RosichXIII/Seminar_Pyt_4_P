# 34). Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю.
# Задача - сформировать файл, содержащий сумму многочленов (суммируем подобные слагаемые).
# Пример:
# 1 Файл : 2*x2 + 4*x + 5 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 6*x2 + 11*x + 14 = 0
# Пример:
# 1 Файл : 2*x3 + 4*x2 + 5*x + 1 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 2*x3 + 8*x2 + 12

import random
import re
from unicodedata import digit
from unittest import skip
polynoms = []
polynom_files_names = ['Polynom_first.txt', 'Polynom_second.txt']
powers_unicode = ['\u00B2', '\u00B3', '\u2074', '\u2075']
for i in range(2):
    polynoms.append('')
    k_power = random.randint(0, 5)
    while k_power > 0:
        coefficient = random.randint(0, 10)
        if k_power > 1:
            if coefficient == 0:
                k_power -= 1
            elif coefficient == 1:
                polynoms[i] += (f'x{powers_unicode[k_power - 2]} + ')
                k_power -= 1
            else:
                polynoms[i] += (f'{coefficient}x{powers_unicode[k_power - 2]} + ')
                k_power -= 1
        else:
            if coefficient == 0:
                k_power -= 1
            elif coefficient == 1:
                polynoms[i] += (f'x{powers_unicode[k_power - 2]} + ')
                k_power -= 1
            else:
                polynoms[i] += (f'{coefficient}x + ')
                k_power -= 1
    if len(polynoms[i]) == 0:
        with open(polynom_files_names[i], 'w', encoding="utf-8") as File:
            File.write('0 = 0')
    else:
        coefficient = random.randint(0, 10)
        if coefficient > 0:
            polynoms[i] += (f'{coefficient} = 0')
        else:
            polynoms[i] = polynoms[i][:-2] + ('= 0')
        with open(polynom_files_names[i], 'w', encoding="utf-8") as File:
            File.write(polynoms[i])

polynom_total = []
for i in range(len(powers_unicode)+2):
    polynom_total.append(0)

powers_alter = []
for i in powers_unicode:
    powers_alter.insert(0, i)

polynom_for_calculations = []
for i in range(2):
    with open(polynom_files_names[i], 'r', encoding="utf-8") as File:
        for line in File:
            polynom_for_calculations.append(re.findall('[^\ +]+', line))
for i in range(2):
    polynom_for_calculations[i].pop(-1)
    polynom_for_calculations[i].pop(-1)

for i in range(2):
    for j in polynom_for_calculations[i]:
        for k in range(len(polynom_total)):
            if k < len(powers_alter):
                if powers_alter[k] in j:
                    if (j[:-2]) != '':
                        polynom_total[k] += int(j[:-2])
                    else:
                        polynom_total[k] += 1
            elif k == (len(polynom_total) - 2):
                if 'x' in j:                                        
                    count = 0
                    l = 0
                    while l < len(powers_alter):
                        if powers_alter[l] in j:
                            count += 1
                            l += 1
                        else:
                            l+= 1
                    if count == 0:
                        if (j[:-1]) != '':
                            polynom_total[k] += int(j[:-1])
                        else:
                            polynom_total[k] += 1
    if 'x' not in j:
        polynom_total[k] += int(j)
if polynom_total == [0, 0, 0, 0, 0, 0]:
    with open('Polynom_total.txt', 'w', encoding="utf-8") as File:
        File.write('0 = 0')
else:
    with open('Polynom_total.txt', 'w+', encoding="utf-8") as File:
        for i in range(len(polynom_total)):
            if polynom_total[i] > 0:
                if i < len(powers_alter):
                    if polynom_total[i] == 1:
                        File.write(f'x{powers_alter[i]} +')
                    else:
                        File.write(f' {polynom_total[i]}x{powers_alter[i]} +')
                elif i == (len(polynom_total) - 2):
                    if polynom_total[i] == 1:
                        File.write(f'x + ')
                    else:
                        File.write(f' {polynom_total[i]}x +')
                else:                    
                    File.write(f' {polynom_total[i]} ')        
        if line[-1] == '+':
            File.out.write(line[:-1])
            File.write('= 0')
        else:
            File.write('= 0')