from fake_math import divide as fk
from true_math import divide as tr

print('\033[96mЗдесь на 0 делить нельзя\033[0m')
result1 = fk(float(input('Введите делимое: ')), float(input('Введите делитель: ')))
print(result1)
print('\033[96mЗдесь на 0 делить можно\033[0m')
result2 = tr(float(input('Введите делимое: ')), float(input('Введите делитель: ')))
print(result2)
