"""
A simple Keyless Encryption module

P15/1730/2017
SAMSON NGULI MUOKI

Requirements = message

Steps
    1. Write message
    2. Convert message to ASCII codes
    2. Convert ASCII codes back to message

How to run
    $ python3 keyless_encryption.py
"""


def write_message():
    # Request user to enter message
    print("\t KEYLESS ENCRYPTION")
    message = str(input("Enter your message: "))
    print(message, "\n")
    message_list = list(message)

    return message_list


def encrypt_message():
    # Encryption process
    message_list = write_message()
    encrypted_message = []

    for char in message_list:
        mapping = ord(char)
        encrypted_message.append(mapping)

    return encrypted_message


def decrypt_message():
    # Decryption process
    encrypted_message = encrypt_message()
    decrypted_mapping = []

    for value in encrypted_message:
        decrypted_value = chr(value)
        decrypted_mapping.append(decrypted_value)

    print(f"Encrypted message is \n {encrypted_message} \n")

    print("\n Decrypted Message is: \n ")
    for char in decrypted_mapping:
        print(char, end="")
    print("\n")


decrypt_message()
