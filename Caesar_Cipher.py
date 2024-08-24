def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = ord(char) + shift_amount

            #checking if the new character exceeds the alphabet's range.
            if char.islower():
                if new_char > ord('z'):
                    new_char -= 26
                encrypted_text += chr(new_char)


            elif char.isupper():
                if new_char > ord('Z'):
                    new_char -= 26
                encrypted_text += chr(new_char)
        else:
            #character is not a letter, it remains unchanged.
            encrypted_text += char

    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    #negative shift value to reverse the encryption process.
    return caesar_cipher_encrypt(text, -shift)

def main():
    
    #program running until the user chooses to exit
    print()
    print("Caesar Cipher Program")
    print()
    print("1. Encrypt")
    print("2. Decrypt")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print()
        print(f"Encrypted message: {encrypted_message}")
        print()

    elif choice == '2':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print()
        print(f"Decrypted message: {decrypted_message}")
        print()
        
    else:
        print("Invalid choice, program will exit.")
        print()
        
if __name__ == "__main__":
    main()