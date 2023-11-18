class Engine:

  def __init__(self, power):
      self.power = power
class Vehicle(Engine):

  def __init__(self, wheels):
      super().__init__(400)
      self.wheels = wheels

  def get_power(self):
      print(self.power)

object2 = Vehicle(4)
object2.get_power()