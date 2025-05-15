import random

#for _ in range(10):
#    print(random.randint(1, 10))

nomes = ['Diego', 'André', 'Paulo', 'Ana', 'Laura']

#print(nomes[random.randint(0, len(nomes) - 1)])

for _ in range(10):
    #print(random.choice(nomes))
    #print(random.sample(nomes, 3))
    ...

print(nomes)
random.shuffle(nomes)
print(nomes)