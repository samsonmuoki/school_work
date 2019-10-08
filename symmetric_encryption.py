"""
A simple Symmetric Encryption module

P15/1730/2017
SAMSON NGULI MUOKI

Requirements = message, encryption key

Steps
    1. Write message
    2. Encrypt message
    2. Decrypt message

How to run
    $ python3 symmetric_encryption.py
"""


def request_encryption_key():
    encryption_key = int(input("Enter an integer for encryption: "))
    if encryption_key == 0:
        print("Encryption key has to be greater than 1")
        request_encryption_key()
    return encryption_key


def request_decryption_key():
    decryption_key = int(input("Enter an integer for decryption: "))
    if decryption_key == 0:
        print("Encryption key has to be greater than 1")
        request_decryption_key()
    return decryption_key


def write_message():
    print("\t SYMMETRIC ENCRYPTION")
    message = str(input("Enter your message: "))
    print(message, "\n")
    message_list = list(message)

    return message_list


def encrypt_message():
    # Encryption process
    message_list = write_message()
    encryption_key = request_encryption_key()
    ordinal_values = []
    encrypted_message = []

    for char in message_list:
        mapping = ord(char)
        ordinal_values.append(mapping)
        encrypted_mapping = mapping*encryption_key
        encrypted_message.append(encrypted_mapping)
    return encrypted_message
    # print(f"Ordinal values are: \n {ordinal_values} \n")


def decrypt_message():
    # Decryption process
    encrypted_message = encrypt_message()
    decryption_key = request_decryption_key()
    decrypted_mapping = []
    decrypted_message_list = []

    for value in encrypted_message:
        decrypted_value = int(value/decryption_key)
        decrypted_mapping.append(decrypted_value)

    for value in decrypted_mapping:
        char = chr(value)
        decrypted_message_list.append(char)

    print(f"Encrypted message is \n {encrypted_message} \n")
    # print(f"Decrypted mapping is: \n {decrypted_mapping} \n")
    # print(f"Message list is: \n {decrypted_message_list} \n")
    print("Decrypted Message is: \n ")
    for char in decrypted_message_list:
        print(char, end="")
    print("\n")


decrypt_message()
