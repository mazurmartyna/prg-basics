###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char != ' ':
        number = ord(char) + 1
        char = chr(number)
    else:    
        char = char
    encrypted_text = encrypted_text + char

    # read the character's code (use ord())
    # add one to the character's code
    # replace new character code with its
    # corresponding character (use chr())
    # add encrypted character to encrypted text

print(plain_text)
print(encrypted_text)