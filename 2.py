total = 0
prev = 0
current = 1

while current < 4_000_000:
  next = current + prev
  prev = current
  current = next

  if next % 2 == 0:
    total += next

print(total)