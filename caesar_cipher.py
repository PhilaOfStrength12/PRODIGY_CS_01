import random

class CaesarCipher:
    # Make the alphabet size a constant value since it is used repetitively
    # Allows you to modify value at one place instead of multiple places which
    # may lead to errors
    ALPHABET_SIZE = 26

    def __init__(self, shift=None):    
        # Setting a default shift value to random number between 1 and 26
        # in case a custom shift value is not provided, if shift value is provided
        # it will be used instead of a random one
        if shift is None:
            shift = random.randint(1, self.ALPHABET_SIZE)
        self.shift = shift

    def encrypt(self, text, shift=None):

        # Since we're using this function for both encryption and decryption,
        # it's helpful to include this code so that it can use either the specified shift value
        # when encrypting or the negative of it if we are decrypting. 
        if shift is None:
            shift = self.shift

        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shift_amount = shift % CaesarCipher.ALPHABET_SIZE
                new_char = ord(char) + shift_amount

                #checking if the new character exceeds the alphabet's range.
                if char.islower():
                    if new_char > ord('z'):
                        new_char -= CaesarCipher.ALPHABET_SIZE
                    encrypted_text += chr(new_char)

                elif char.isupper():
                    if new_char > ord('Z'):
                        new_char -= CaesarCipher.ALPHABET_SIZE
                    encrypted_text += chr(new_char)
            else:
                #character is not a letter, it remains unchanged.
                encrypted_text += char
        
        return encrypted_text

    def decrypt(self, encrypted_text):
        #negative shift value to reverse the encryption process.
        return self.encrypt(encrypted_text, -self.shift)