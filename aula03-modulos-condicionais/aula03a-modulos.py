from math import sqrt
import random

num = random.randint(2, 100)

raiz = sqrt(num)

print(f"A raiz quadrada de {num} é: {raiz:.2f}")

num_rand = random.random()
print(f"número aleatorio {num_rand*10:.2f}")

num_rand_int = random.randint(1, 60)
print(num_rand_int)