## Number 1 

phonebook_dict = { 
  'Alice': '703-493-1834', 
  'Bob': '857-384-1234', 
  'Elizabeth': '484-584-2923'
}

elizabeth_1 = phonebook_dict['Elizabeth']
print('Elizabeths Number: ' + elizabeth_1)

phonebook_dict['Kareem'] = '938-489-1234'

del phonebook_dict['Alice']

phonebook_dict['Bob'] = '968-345-2345'

print(phonebook_dict)

## Number 2 - Nested

ramit = { 
  'name': 'Ramit', 
  'email': 'ramit@gmail.com', 
  'interests': ['movies', 'tennis'], 
  'friends': [ 
     { 
       'name': 'Jasmine', 
       'email': 'jasmine@yahoo.com', 
       'interests': ['photography', 'tennis']
     }, 
     { 
        'name': 'Jan', 
        'email': 'jan@hotmail.com', 
        'interests': ['movies', 'tv'] 
     } 
    ] 
}

print(ramit["email"])
print(ramit['interests'][0])
print(ramit['friends'][0]['email'])
print(ramit['friends'][1]['interests'][1])

## Letter Summary

word = input("Pick a word: ")
letter_dictionary = {
      
}

for character in word:
    letter_dictionary[character] = word.count(character)
print(letter_dictionary)

# Word Summary

phrase = input("Pick a phrase: ")
word_dictionary = {
      
}
word_histogram = phrase.split()

for word in word_histogram:
    word_dictionary[word] = phrase.count(word)
print(word_dictionary)




