import random

r = int(input('Введите диапозон чисел:'))
b = int(input('Введите количество элементов:'))

massive = random.sample(range(r), b)
#/ list(map(int, input().split()))
move = 0

for run in range(b-1):
    for i in range(b-1-run):
        if massive[i] > massive[i+1]:
            move += 1
            massive[i],massive[i+1] = massive[i+1],massive[i]

print(*massive)
print(move)
