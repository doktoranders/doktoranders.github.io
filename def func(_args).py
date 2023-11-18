def multiply_numbers(*args):
  result = 1
  for number in args:
    result *= number
  return result

n1 = int(input('Enter a number: '))
n2 = int(input('Enter a second number: '))
n3 = int(input('Enter a third number: '))

result = multiply_numbers(n1, n2, n3)

print(result)