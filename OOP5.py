class Triangle:
  """A class representing a triangle"""
  def __init__(self, a, b, c):
      """
      Initialize the triangle with side lengths a, b, and c
      """
      self.a = a
      self.b = b
      self.c = c
  def get_perimeter(self):
      """
      Calculate the perimeter of the triangle
      """
      perimeter = self.a + self.b + self.c
      return perimeter
if __name__ == "__main__":
  try:
      a = int(input('Enter side 1 in a triangle: '))
      b = int(input('Enter side 2 in a triangle: '))
      c = int(input('Enter side 3 in a triangle: '))
      new_triangle = Triangle(a, b, c)
      result = new_triangle.get_perimeter()
      print(result)
  except ValueError:
      print("Please enter a valid number for side length")