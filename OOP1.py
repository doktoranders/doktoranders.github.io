class Person:

  def __init__(self, attr1):
    self.greeting = attr1

  def greet(self):
    print(self.greeting)


greeting = input('Enter a greeting: ')

person1 = Person(greeting)

person1.greet()
