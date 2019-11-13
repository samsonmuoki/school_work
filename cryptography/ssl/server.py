"""A simple SSL server module.

    P15/1730/2017
    SAMSON NGULI MUOKI


"""

import socket
from math import gcd


p, q = 101, 103


def product():
    # Find n
    n = p*q
    return n


def find_totient():
    # Find totient(n)
    totient = (p-1)*(q-1)
    return totient


def find_public_key_exponent():
    # Find public key exponent k
    co_primefactors_to_totient = []
    totient = find_totient()
    for i in range(2, totient):
        if gcd(i, totient) == 1:
            co_primefactors_to_totient.append(i)
    public_key_exponent = co_primefactors_to_totient[0]
    return public_key_exponent


public_key = (str(product()) + '-' + str(find_public_key_exponent()))
print(f"Public Key = {public_key} \n")


def find_private_key_exponent():
    # Find secret key exponent
    totient = find_totient()
    secret_key_exponents = []
    public_key_exponent = find_public_key_exponent()
    for i in range(1, totient):
        """
        k*d == 1 + (i * totient) so
        d = (1 + (i*totient))/k
        """
        if (1 + (i*totient)) % public_key_exponent == 0:
            secret_key_exponent = int((1 + (i*totient))/public_key_exponent)
            secret_key_exponents.append(secret_key_exponent)
    secret_key_exponent = secret_key_exponents[0]
    return secret_key_exponent


private_key = [p, q, find_private_key_exponent()]
# print(f"Private key Exponent= {find_private_key_exponent()} \n")
print(f"Private key= {private_key} \n")


# SOCKET COMMUNICATION STARTS HERE
HOST = "127.0.0.1"
PORT = 65432


server_public_key = str(public_key)
server_public_key_bytes = server_public_key.encode('utf-8')

print("Waiting for connections...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by ", addr)
        # Receive hello message from client
        client_handshake_message = conn.recv(1024)
        client_handshake_message = client_handshake_message.decode('utf-8')
        print(f"\n Handshake message: {client_handshake_message}\n ")

        # Send hello message to client plus public key
        server_handshake_message = 'Hello client, ' + 'Here is my public key:' + str(server_public_key)
        server_handshake_message = server_handshake_message.encode('utf-8')
        conn.sendall(server_handshake_message)

        # Receive encrypted symmetric key from client
        encrypted_client_key = conn.recv(1024)
        encrypted_client_key = int(encrypted_client_key.decode('utf-8'))
        print(f"\n Here is my encrypted client key: {encrypted_client_key} \n")

        # Decrypt client key
        decrypted_key = (encrypted_client_key**find_private_key_exponent()) % product()
        print(f"Decrypted key is: {decrypted_key} \n")

        # Send acknowledgement to client
        conn.sendall(b'Symmetric key received successfully')

        while True:
            # Receive message from client
            data = conn.recv(1024)
            decoded_data = data.decode('utf-8')
            print(f"Received message: {decoded_data} \n")
            data_list = decoded_data.split('-')
            # print(data_list)

            # Decode message
            print("Decrypted message is: \n")
            normal_character_array = []
            for i in data_list:
                normal_ord_value = int(int(i)/int(decrypted_key))
                normal_character = chr(normal_ord_value)
                normal_character_array.append(normal_character)
                print(normal_character, end='')
            print("\n")
