# Number 1 - Uppercase a String
string_1 = 'Hello World'
print('1) Uppercase of Hello World: ' + string_1.upper())

# Number 2 - Capitalize a String
string_2 = 'hello mars'
print('2) Capitalizing hello mars: ' + string_2.capitalize())


# Number 3 - Reverse a String
string_3 = 'never odd or even'
print('3) Reversing a string "Never odd or even": ' + string_3[::-1])

# Number 4 - Leetspeak
leet_speak = 'I WANT TO BREAK FREE'
print('4) Given the following letters: ')
print('A => 4 E => 3 G => 6 I => 1 O => 0 S => 5 T => 7')

for i in leet_speak:
    if i == 'A':
        leet_speak = leet_speak.replace("A" , "4")
    if i == 'E':
        leet_speak = leet_speak.replace("E" , "3")
    if i == 'G':
        leet_speak = leet_speak.replace("G" , "6")
    if i == 'I':
        leet_speak = leet_speak.replace("I" , "1")
    if i == 'O':
        leet_speak = leet_speak.replace("O" , "0")
    if i == 'S':
        leet_speak = leet_speak.replace("S" , "5")
    if i == 'T':
        leet_speak = leet_speak.replace("T" , "7")


print('Using the sentence "I WANT TO BREAK FREE" and replacing with Leetspeak: ' + leet_speak)                            
    
# Number 5 - Long-long Vowels
string_5a = "I want to break free"
string_5b = ['a' , 'e' , 'i' , 'o' , 'u']
sent = ""

if string_5a.find(string_5b[0]) >= 0:
    string_5a = string_5a.replace("a", "aaaaaaa")
if string_5a.find(string_5b[0]) >= 0:
    string_5a = string_5a.replace("e", "eeeeeee")
if string_5a.find(string_5b[0]) >= 0:
    string_5a = string_5a.replace("i", "iiiiiii")
if string_5a.find(string_5b[0]) >= 0:
    string_5a = string_5a.replace("o", "ooooooo")
if string_5a.find(string_5b[0]) >= 0:
    string_5a = string_5a.replace("u", "uuuuuuu")             

print(string_5a)

# Number 6 - Ceaser Cipher
cipher = 'lbh zhfg hayrnea jung ibh unir yrnearq'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

position = 0
new_position = 0
final_string = ''

for cipher_letter in cipher:
    if cipher_letter.isspace() == False:
        position = alphabet.index(cipher_letter)
        new_position = position - 13
        if new_position < 0:
            new_position = 26 + new_position
        final_string = str(final_string) + alphabet[new_position]    
        

print('6) The cipher decoded says "You must unlearn what you have learned: ' + final_string)        
