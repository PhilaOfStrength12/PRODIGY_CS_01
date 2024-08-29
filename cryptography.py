from caesar_cipher import CaesarCipher

if __name__ == "__main__":
    text = "Love"

    '''
    EXAMPLE 1
     Initializing the Cipher without a specified shift
     The shift will be random between 1 and 26
    '''
   
    random_cipher = CaesarCipher()
    print(f"Generated Shift: {random_cipher.shift}")

    encrypted_text = random_cipher.encrypt(text)
    print(f"Encrypted: {encrypted_text}")

    decrypted_text = random_cipher.decrypt(encrypted_text)
    print(f"Decrypted: {decrypted_text}")

    '''
    EXAMPLE 2
     Initializing the Cipher with a specified shift
     The shift will be the specified shift value
    '''

    specific_cipher = CaesarCipher(shift=4)
    print(f"\nGenerated Shift: {specific_cipher.shift}")

    encrypted_text = specific_cipher.encrypt(text)
    print(f"Encrypted: {encrypted_text}")

    decrypted_text = specific_cipher.decrypt(encrypted_text)
    print(f"Decrypted: {decrypted_text}")
