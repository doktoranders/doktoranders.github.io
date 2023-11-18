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

list1 = [object1, object2, object3, object4, object5]
for object in list1:
  print(object)