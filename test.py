import random

nombres = [random.randint(145, 150) for _ in range(200)]
resultat = ', '.join(map(str, nombres))

print(resultat)
