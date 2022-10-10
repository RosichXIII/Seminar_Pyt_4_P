# 30). Вычислить число π c заданной точностью d
# Пример:
# при d = 0.001,π = 3.141 10^(-1)≤d≤10^(-10)

from decimal import Decimal
from decimal import ROUND_FLOOR
import math
from math import acos

precision_d = input('Введите желаемую точность числа π (в формате: d = 1.0; d = 1.000...)\n')
calculated_pi = Decimal(round(2 * acos(0.0), 30))
print('Результат:', calculated_pi.quantize(Decimal(f"{precision_d}"), ROUND_FLOOR))
print('Проверочная константа π:', math.pi)