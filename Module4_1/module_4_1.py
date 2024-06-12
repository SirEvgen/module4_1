from fake_math import divide as fk
from true_math import divide as tr

print('Здесь на 0 нельзя делить')
result1 = fk(float(input('Введите делимое: ')), float(input('Введите делитель: ')))
print(result1)
print('Здесь на 0 можно делить')
result2 = tr(float(input('Введите делимое: ')), float(input('Введите делитель: ')))
print(result2)
