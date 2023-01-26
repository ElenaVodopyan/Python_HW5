import random
numbers = list(random.randint(1, 10) for _ in range(random.randint(5, 20)))
print(f'Список случайных чисел: {numbers}')
result = []
for el in numbers:
    if (el not in result): 
        result.append(el)
print(f'Список уникальных элементов: {set(result)}')