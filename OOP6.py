class Polygon:
  def __init__(self, sides):
      self.sides = sides

  def display_info(self):
      print("A polygon is a two dimensional shape with straight lines.")

  def get_perimeter(self):
      perimeter = sum(self.sides)
      return perimeter

class Triangle(Polygon):
  def display_info(self):
      print("A triangle is a polygon with 3 edges.")

# create an object of Triangle
t1 = Triangle([5, 6, 7])

# call get_perimeter using t1
perimeter = t1.get_perimeter()
print("Perimeter:", perimeter)

# call display_info() using t1
t1.display_info()