from itertools import product

K, M = map(int, input().split())

lists = []

for _ in range(K):
    data = list(map(int, input().split()))
    lists.append(data[1:])   # Skip Ni

result = max(
    sum(x*x for x in combination) % M
    for combination in product(*lists)
)

print(result)
