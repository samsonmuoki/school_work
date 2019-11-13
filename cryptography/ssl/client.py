"""A simple client module.

    P15/1730/2017
    SAMSON NGULI MUOKI


"""

import socket


# SOCKET COMMUNICATION STARTS
HOST = "127.0.0.1"
PORT = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect and send hello message to server
    s.connect((HOST, PORT))
    s.sendall(b'Hello Server')

    # Receive hello message from server
    hanshake_message = s.recv(1024)
    hanshake_message = hanshake_message.decode('utf-8')
    print(f"\nHandshake message: {hanshake_message} \n")
    server_public_key = (hanshake_message.split(':')[-1]).split('-')
    product, public_key_exponent = int(server_public_key[-2]), int(server_public_key[-1])

    # Request a symmetric key for encryption and decryption
    symmetric_key = int(input('Enter a random integer for encryption: '))
    client_key = str(symmetric_key)
    client_key_bytes = client_key.encode('utf-8')

    # Encrypt symmetric key using public key and send to server
    cipher_client_key = (int(symmetric_key) ** public_key_exponent) % product
    cipher_client_key = str(cipher_client_key).encode('utf-8')
    s.sendall(cipher_client_key)

    acknowledgement_message = s.recv(1024)
    acknowledgement_message = acknowledgement_message.decode('utf-8')
    print(f"\n {acknowledgement_message} \n")

    while True:
        # Request user a message
        message = input("\n Enter your message: \n")

        # Encrypt message
        message_list = list(message)
        cipher_values = []
        for i in message_list:
            ord_string = str(ord(i)*symmetric_key)
            cipher_values.append(ord_string)
        # print(cipher_values)
        cipher_text = '-'.join(cipher_values)
        cipher_bytes = cipher_text.encode('utf-8')
        # print(cipher_bytes)

        # Send encrypted message to server
        s.sendall(cipher_bytes)
