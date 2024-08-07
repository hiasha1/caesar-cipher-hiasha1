

text = input('please enter the string \n')
shift = 5
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    
    if char.isalpha()==False:
        print(char, end = '' )
        
    else:
        index = alphabet.find(char)
        new_index = (index + shift) % len(alphabet)
        encrypted_text = alphabet[new_index]
        print( encrypted_text ,end = '')


