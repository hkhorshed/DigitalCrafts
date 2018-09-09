# $ python phonebook.py 
# Electronic Phone Book 
# ===================== 
# 1. Look up an entry 
# 2. Set an entry 
# 3. Delete an entry 
# 4. List all entries 
# 5. Quit


phonebook_ditionary = {
    'Hussein' : '713-373-9507',
    'Bob' : '281-494-3760',
    'Skylar' : '832-541-6713' 
}

pba = input('Press 1, 2, 3, 4, or 5 to here your options. ')

for i in pba:
    if pba == '1':
        entry_1 = input('Type the name: ')
        get_1 = phonebook_ditionary .get(entry_1)
        print(get_1)
    elif pba == '2':
        entry_2a = input('Type the name: ')
        entry_2b = input('Number:')
        phonebook_ditionary[entry_2a] = entry_2b 
        print('Name ' + str(entry_2a) + ' Phone: ' + str(entry_2b) )
    elif pba == '3':
        entry_3 = input('Who do you wish to delete ')
        del phonebook_ditionary[entry_3]
        print('This entry ' + str(empty_3) + ' has been deleted.')
    elif pba == '4':
        print(phonebook_ditionary)
    else:
        pba = 'Quit'
        break






