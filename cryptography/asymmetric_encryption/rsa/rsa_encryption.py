"""
    A simple implementation of RSA algorithm

    P15/1730/2017
    Samson Nguli Muoki

    Requirements
        2 large random prime numbers = p, q
        n = p*q
        totient(n) = (p-1)(q-1)

        public key exponent = int(k), k is co-prime to totient(n):
            1 < k < totient(n)
            gcd(k,totient(n)) = 1
            popular choice == 2^16 + 1 == 65537

        private key exponent = d:
            1 < d < totient(n)
            k*d == 1 mod (totient(n)):
                d == (1 mod (totient(n)))/k
            k*d == 1 + x*totient(n) for some int(x)
            int(d) = 1 + (x*totient(n))/k

"""


from math import gcd


p, q = 101, 103


def write_message():
    message = input("Enter your message: ")
    message_list = list(message)
    return message_list


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


public_key = [product(), find_public_key_exponent()]
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
print(f"Private key = {private_key} \n")


def encrypt_message():
    # Encrypt message
    message_list = write_message()
    padded_message = []
    for i in message_list:
        padded_character = str(ord(i))
        padded_message.append(padded_character)

    cipher_text = []
    public_key_exponent = find_public_key_exponent()
    n = product()
    for i in padded_message:
        cipher_character = (int(i) ** public_key_exponent) % n
        cipher_text.append(cipher_character)
    return cipher_text


cipher_text = encrypt_message()
print(f"Cipher text is: {cipher_text} \n")


def decrypt_message():
    decrypted_cipher = []
    private_key_exponent = find_private_key_exponent()
    n = product()
    for i in cipher_text:
        decrypted_value = (i**private_key_exponent) % n
        decrypted_cipher.append(decrypted_value)

    decrypted_message_list = []
    for i in decrypted_cipher:
        normal_character = chr(i)
        decrypted_message_list.append(normal_character)
    # return decrypted_message_list

    print(f"Decrypted message is: \n")
    for i in decrypted_message_list:
        print(i, end="")
    print("\n")


decrypt_message()
