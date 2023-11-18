def add_numbers(*numbers):
  total = 0
  for number in numbers:
      total = total + number
  return total

result = add_numbers(5, 10)
print(result)    

result = add_numbers(5, 10, 20)
print(result) 