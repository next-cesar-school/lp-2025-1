# -*- coding: utf-8 -*-


def fibonacci(start):
    numbers = [0]

    if start > 1:
        numbers.append(1)

    for _ in range(start - 2):
        numbers.append(numbers[-1] + numbers[-2])

    return numbers

num = int(input())
print(*fibonacci(num))
