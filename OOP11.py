class Bicycle:
  def __init__(self, gear, speed):
      # initialize attributes
      self.gear = gear
      self.speed = speed

  # create the print_atributes() method 
  def print_attributes(self):
      print(self.gear)
      print(self.speed)

# create the object with 4 and 80 as arguments
bicycle1 = Bicycle(4, 80)

# call print_atributes() using bicycle1
bicycle1.print_attributes()