# Number 1 - Sum the Numbers

myList = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
print('This is my list for the homework: ' + str(myList))

sumList = sum(myList)
print('1) The sum of myList: ' + str(sumList))

# Number 2 - Largest Number

largest_number = max(myList)
print('2) The largest number of myList: ' + str(largest_number))

# Number 3 - Smallest Number

smallest_number = min(myList)
print('3) The smallest number of myList: ' + str(smallest_number))

# Number 4 - Even Numbers

even_numbers = myList[0 : 11 : 2]
print('4) These are all the even numbers: ' + str(even_numbers))

# Number 5 - Positive Numbers

positive_numbers = []
for i in myList:
    if i > 0:
        positive_numbers.append(i)

print('5) The numbers greater than zero are: ' + str(positive_numbers))

# Number 6 - Positive Numbers II

positive_numbers_II = []
for i in myList:
    if i > 0:
        positive_numbers_II.append(i)

print('6) These numbers are all positive: ' + str(positive_numbers_II))

# Number 7 - Multiply a Number

factor = 2
multiply_a_number = []
for i in myList:
    i = i * 2
    multiply_a_number.append(i)

print('7) This is multplying my list by a factor of 2: ' + str(multiply_a_number))

# Number 8 - Multiplying Vectors
a = [2 , 5 , 7]
b = [1 , 4 , 2]
print('8) These are the vectors being used ')
print('Vector a: ' + str(a))
print('Vector b: ' + str(b))
a_dot_b = []
count = 0
product = 0

for n in a:
    product = n * b[count]
    a_dot_b.append(product)
    count += 1    

print('This is the multiplication of the two vectors a and b: ' + str(a_dot_b))

# Number 9 - Matrix Additions 
c = [[1 , 3] , [5 , 7]]
d = [[0 , 2] , [4 , 6]]

print('9) These are the matrices being added ')
print('Matrix c: ' + str(c))
print('Matrix d: ' + str(d))

mat_add = []

for i in range(len(c)):
    row = []
    for j in range(len(c[0])):
        row.append(c[i][j] + d[i][j])
    mat_add.append(row)


print('This is the addition of the two vectors c and d: ' + str(mat_add))

#Number 10 - Matrix Addition II

matrix_a = [[1 , 3] , [5 , 7] , [5 , 8]]
matrix_b = [[0 , 2] , [4 , 6] , [3 , 7]]

print('10) These are the matrices being added ')
print('Matrix_a: ' + str(matrix_a))
print('Matrix_b: ' + str(matrix_b))

mat_add = []

for i in range(len(matrix_a)):
    row = []
    for j in range(len(matrix_a[0])):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    mat_add.append(row)


print('This is the addition of matrix_a and matrix_b: ' + str(mat_add))

# Number 11 - De-dup
list_11a = "i zamz reallybb ticcred"
list_11b = ""

seen = set(list_11a)

print('11) ' + str(seen))





