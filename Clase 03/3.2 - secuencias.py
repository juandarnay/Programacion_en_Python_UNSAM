data = [4, 9, 1, 25, 16, 100, 49]
print(min(data))
print(max(data))
print(sum(data))

for d in data:
    print(d)

for n, d in enumerate(data):
    print(n, d)

for n in range(len(data)):
    print(data[n])