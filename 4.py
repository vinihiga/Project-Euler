result = 0

def is_palindrome(value: str) -> bool:
  left_ptr = 0
  right_ptr = len(value) - 1

  while left_ptr < right_ptr:
    if value[left_ptr] != value[right_ptr]:
      return False
    
    left_ptr += 1
    right_ptr -= 1

  return True

# This algorithms iterates O(n^2)
# Is there somehow to be faster?
for lhs in range(100, 1000):
  for rhs in range(100, 1000):
    total = lhs * rhs
    if is_palindrome(str(total)) and total > result:
      result = total

print(result)