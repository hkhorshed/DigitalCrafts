# Number 1
loop_1 = []
for i in range(1 , 11):
    loop_1.append(i)
    i += 1
    
print('1) A for loop that prints out 1 through 10 ' + str(range(i)))

# Number 2

n = int(input('What is your value for n? '))
m = int(input('What is your value for m? '))

loop_2 = []

for i in range(n , m):
    loop_2.append(i)

print(loop_2)

# Number 3

loop_3 = []

for i in range(1 , 11):
    if i % 2 == 0:
        loop_3.append(i - 1)
    else:
        i += 1

print(loop_3)

# Number 4

size_4 = 5

for i in range(size_4):
    print('*' * size_4)

# Number 5
size_5 = int(input('How big do you want the square? '))

for i in range(size_5): 
    print('*' * size_5) 

# Number 6

n = int(input('6) What is the size of your square? '))

for i in range(n-2):
    print ('*' + ' ' * (n-2) + '*')

print('*' * n)

## Number 7
t = int(input('7) What is the value for t to assign to the triangle? '))
print('\n'.join(['*' * i for i in range(1 ,t + 1)]))

# Number 8

height = int(input("Height of triangle: "))
count = 0

for i in range(height - 1):
    print('*' + ' ' * count + '*')
    count += 1

print('*' * height)

# Number 9

x = int(input("Display multiplication table of? "))

for i in range(1, x + 1):
   print(str(x) + ' x ' + str(i) + ' = ' + str((x * i)))
