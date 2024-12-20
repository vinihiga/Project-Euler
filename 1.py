total = 0

for e in range(1000):
  if e % 3 == 0 or e % 5 == 0:
    total += e

print(total)