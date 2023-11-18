class Person:
  def __init__(self, name, age):
      self.current_name = name
      self.current_age = age

  def print_data(self, name, age):
    print(f"Name: {name}\n Age: {age}")


person_list = []
while True:
  name = input('Enter a name: ')
  age = int(input('Enter an age: '))
  person_list.append(Person(name, age))
  answer = input("Do you want to continue? (y/n) ")
  if answer == 'n':
    break
for person in person_list:
  person.print_data(name, age)