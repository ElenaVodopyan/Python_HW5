import random
numbers = list(random.randint(1, 10) for _ in range(random.randint(5, 20)))
print(f'Список случайных чисел: {numbers}')
result = list(filter(lambda x: x > 5, numbers))
print(f'Список больше 5: {result}')