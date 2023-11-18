class Triangle:

  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def get_perimeter(self, x, y, z):
      perimeter = x + y + z
      return perimeter

a = int(input('Value 1; '))
b = int(input('Value 2: '))
c = int(input('Value 3: '))

object1 = Triangle(a, b, c)

perimeter = object1.get_perimeter(a, b, c)

print(perimeter)