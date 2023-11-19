class Person:
  def __init__(self, person_name, person_age):
      self.name = person_name
      self.age = person_age

  def display_info(self):
      print(f'Name: {self.name}, Age: {self.age}')

def create_person_list(num_people):
  person_list = []
  for _ in range(num_people):
      name = input('Enter name: ')
      age = int(input('Enter age: '))
      person = Person(name, age)
      person_list.append(person)
  return person_list

def main():
  num_people = 3
  people = create_person_list(num_people)
  for person in people:
      person.display_info()
  return(people)

if __name__ == "__main__":
  main()