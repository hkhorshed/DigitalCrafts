# # Number 1 - Basics

class Person: 
    def __init__(self, name, email, phone, friends , count): 
        self.name = name 
        self.email = email 
        self.phone = phone 
        self.friends = []
        self.count = 0
    def greet(self, friend): 
        print('Hello {}, I am {}!'.format(friend.name, self.name))
        self.greeting_count()
    def contact_info(self):
        print(self.name , self.email , self.phone)
    
    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        print(len(self.friends))

    def greeting_count(self):
        self.count += 1
        print(self.count)

    def __reset_count(self):
        self.count = 0
        
        


sonny = Person('Sonny' , 'sonny@hotmail.com' , '483-485-4948' , [] , 0)
jordan = Person('Jordan' , 'jordan@aol.com' , '495-586-3456' , [] , 0)

# sonny.greet(jordan)
# jordan.greet(sonny)

# sonny.contact_infor()
# jordan.contact_infor()

jordan.friends.append(sonny)
sonny.add_friend(jordan)

sonny.num_friends()
sonny.greet(jordan)
sonny.greeting_count()
print(sonny.greeting_count())



# # Number 2 - Make your own class

class Vehicle:
    def __init__(self , make , model , year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(car.year , car.model , car.year)

car = Vehicle('Nissan' , 'Leaf' , 2015)

car.print_info()

# Number 3

def __str__(self): 
     return 'Person: {} {} {}'.format(self.name, self.email, self.phone)


    









