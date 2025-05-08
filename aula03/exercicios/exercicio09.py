def fatorial(n):
    total = 1
    for number in range(1, n+1):
        total *= number
    return total

print(fatorial(5))
print(fatorial(6))
print(fatorial(7))
print(fatorial(8))
print(fatorial(9))
print(fatorial(10))
