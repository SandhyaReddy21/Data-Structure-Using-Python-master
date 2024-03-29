'''
Description      :  Data Structure Using Dictionary 
Function Date    :  07 Feb 2024
Function Author  : Sandhya Sampate
Input            :  str
Output           :  str

'''

# 'ab' is short for 'a'ddress'b'ook
ab = { 
        'Swaroop' : 'swaroop@swaroopch.com',
        'Larry' : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer' : 'spammer@hotmail.com'
    }

print ("Swaroop's address is", ab['Swaroop'])

# Deleting a key-value pair

del ab['Spammer']

print ('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print ('Contact {} at {}'.format(name, address))

# Adding a key-value pair

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print ("\nGuido's address is", ab['Guido'])
