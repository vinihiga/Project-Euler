primes = set()

cur = 600851475143
divider = 2

while cur > 1:
  if cur % divider == 0:
    cur = cur / divider
    primes.add(divider)
  else:
    divider += 1

sorted_primes = list(primes)
sorted_primes.sort()
print(sorted_primes[-1])