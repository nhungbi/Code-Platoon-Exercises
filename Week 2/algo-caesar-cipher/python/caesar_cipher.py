def find_shifted_char(char, shift_amount):
    """
    Given a lowercase character, return the shifted character.
    """
    #ord() - 96 will give the ASCII value
    #chr() + 96 will give thhe ASCII value
    char_value = ord(char) - 96
    new_value = (char_value + shift_amount) % 26 #will wrap if need to
    if new_value == 0: #special case
        new_value = 26 #reset to the end
    return chr(new_value+96)

def caesar_cipher(string, shift_amount):
    """
    Given a string and a shift amount, return a new string with each character shifted by that amount.
    """
    shifted_string = ''

    for char in string:
        if char.islower():
            shifted_string += find_shifted_char(char, shift_amount)
        elif char.isupper():
            new_char = find_shifted_char(char.lower(), shift_amount)
            shifted_string += new_char.upper()
        else:
            shifted_string += char

    return shifted_string
    



# print(ord('b') - 96)
# print(chr(97))
# print(caesar_cipher("Boy! What a string!", -5))
# print(caesar_cipher("Hello Zach168! Yes here.", -5))
# print(find_shifted_char('e', -5))