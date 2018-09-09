

# Number 1
name = input('What is your name? ')
print("Hello " + name)

## Number 2
name1 = input('WHAT IS YOUR NAME? ')
print(('HELLO ' + name1.upper() + '! YOUR NAME HAS ' + str(len(name1)) + ' LETTERS'))

## Number 3
country = 'Egypt'
age = 25
sentence = 'I am from %s, and I am %d years old ' %(country , age)
print(sentence)

# Number 4
days_of_week = ['sunday' , 'monday' , 'tuesday' , 'wedensday' , 'thursday' , 'friday' , 'saturday']
day_number = input('Which number do you choose? ')
week_day = days_of_week[int(day_number)]

print(week_day)

# Number 5
if day_number < 6 and day_number > 0:
    print('Go to work')
else:
    print('Sleep in!')

# Number 6
c = input("What is the temperature in Celsius? ")
f = (c * 1.8) + 32
print('The temperature in Farenheit is ' + str(f))

# Number 7
bill = input('What is the total bill? ')
bill1 = int(bill)
service = input('How was the service? ')
tip = str(service)
tip_calc = 0
if service == 'good':
    print(0.2 * bill1)
    tip_calc = 0.2 * bill1
elif service == 'fair':
    print(0.15 * bill1)
    tip_calc = 0.15 * bill1
else:
    print(0.1 * bill1)
    tip_calc = 0.1 * bill1

total_bill = tip_calc + bill1
print(total_bill)

# Number 8
no_of_people = input('How many people? ')
split = total_bill / no_of_people
print(split)

# Number 9
i = 0
while i < 11:
    print(i)
    i += 1

# Number 10
coin = input('Do you want a coin ')
i = 0
while coin == 'yes':
    i += 1 
    print(i)
    coin = input('Do you want another? ')
if coin == 'no':
    print(i)





