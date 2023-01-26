import random
numbers = list(random.randint(1, 1000) for _ in range(random.randint(10, 20)))
print(f'Список случайных чисел: {numbers}')
index = random.randint(0, len(numbers)-1)
result = [numbers[index]]
while index < len(numbers):
    index = random.randint(index, len(numbers))
    if index != len(numbers) and numbers[index] > result[-1]:
        result.append(numbers[index])
print(result)