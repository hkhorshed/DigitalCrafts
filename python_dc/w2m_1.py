class Car:
    def __init__(self , make , model , color):
        self.model = model
        self.make = make
        self.color = color
    
    def change_color(self , new_color):
        print('Changing from {} to {}'.format(self.color , new_color))
        self.color = new_color


michael = Car('Mazda' , 'CX-5' , 'Gray')

michael.change_color('purple')
print(michael.color)

class ElectricCar(Car):
    def __init__(self, make , model , color , range_a , autopilot):
        super().__init__(make , model , color)
        self.range_a = range_a
        self.autopilot = autopilot

keith = ElectricCar('Tesla' , 'Model 3' , 'Black' , 300 , True)

print(keith.make)

    


