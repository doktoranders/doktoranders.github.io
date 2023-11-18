class Bikes:
  def __init__(self, make, model):
      self.make = make
      self.model = model

  def __str__(self):
      return f'Bike make: {self.make}, model: {self.model}'

object1 = Bikes('Kawasaki', 'Ninja')
object2 = Bikes('Yamaha', 'MT09')
object3 = Bikes('Suzuki', 'GSX-S1000R')
object4 = Bikes('Honda', 'CBR1000RR')
object5 = Bikes('Suzuki', 'GSX-S1000RR')

list1 = []
list1.append(object1)
list1.append(object2)
list1.append(object3)
list1.append(object4)
list1.append(object5)

for bike in list1:
  print(bike)

  