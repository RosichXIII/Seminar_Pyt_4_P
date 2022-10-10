# 33). Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k и приравняйте его к нулю.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 2*x*2 + 4*x + 5 = 0
# или
# 2*x^2 + 4*x + 5 = 0

import random
polynom = ''
k_power = random.randint(1, 9)
with open('Polynom_k.txt', 'w', encoding="utf-8") as File:
    File.write(f'Степень k: {str(k_power)}\n')
powers_unicode = ['\u00B2', '\u00B3', '\u2074', '\u2075', '\u2076', '\u2077', '\u2078', '\u2079']
while k_power > 0:
    coefficient = random.randint(0, 100)
    if k_power > 1:
        if coefficient == 0:
            k_power -= 1
        elif coefficient == 1:
            polynom += (f'x{powers_unicode[k_power - 2]} + ')
            k_power -= 1
        else:
            polynom += (f'{coefficient}x{powers_unicode[k_power - 2]} + ')
            k_power -= 1
    else:
        if coefficient == 0:
            k_power -= 1
        elif coefficient == 1:
            polynom += (f'x{powers_unicode[k_power - 2]} + ')
            k_power -= 1
        else:
            polynom += (f'{coefficient}x + ')
            k_power -= 1
if len(polynom) == 0:
    with open('Polynom_k.txt', 'a', encoding="utf-8") as File:
        File.write('Случилось маловероятное - все коэффициенты равны "0", следовательно: 0 = 0.')
else:
    coefficient = random.randint(0, 100)
    if coefficient > 0:
        polynom += (f'{coefficient} = 0')
    else:
        polynom = polynom[:-2] + ('= 0')
    with open('Polynom_k.txt', 'a', encoding="utf-8") as File:
        File.write(polynom)