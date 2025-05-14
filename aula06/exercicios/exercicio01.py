numbers = [1, 3, 2, 3, 4, 5, 1, 5, 7, 6, 8, 3, 4]
set_numbers = set()

for item in numbers:
    set_numbers.add(item)

print(set_numbers)


# Alternativa:
numbers = [1, 3, 2, 3, 4, 5, 1, 5, 7, 6, 8, 3, 4]
set_numbers = set(numbers)

print(set_numbers)
