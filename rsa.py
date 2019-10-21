
from math import gcd
# Find p and q
p, q = 59, 53
print(f"Prime numbers are: {p} and {q}")

# Find n
n = p*q
print(f"n = {n}")

# Find totient(n)
totient = (p-1)*(q-1)
print(f"Totient(n) = {totient} \n")

# Find public key exponent k
co_primefactors_to_totient = []
for i in range(2, totient):
    if gcd(i, totient) == 1:
        # print(i)
        co_primefactors_to_totient.append(i)
        # break

public_key_exponent = co_primefactors_to_totient[0]
public_key = [n, public_key_exponent]

# print(f"Co-prime factors to totient = {co_primefactors_to_totient}")
print(f"Public key exponent = {public_key_exponent} \n")
print(f"Public Key = {public_key} \n")


# Find secret key exponent
secret_key_exponents = []
for i in range(1, totient):

    if (1 + (i*totient)) % public_key_exponent == 0:
        secret_key_exponent = int((1 + (i*totient))/public_key_exponent)
        secret_key_exponents.append(secret_key_exponent)
        # print(
        #     f"For some integer = {i}, Secret Key exponent = {secret_key_exponent}"
        #     )
secret_key_exponent = secret_key_exponents[0]
private_key = [p, q, secret_key_exponent]
# print(f"Secret key exponents = {secret_key_exponents}")
print(f"Secret key exponent = {secret_key_exponent} \n")
print(f"Private key = {private_key} \n")
    
message = input("Enter your message: ")
message_list = list(message)
print(f"Message list: {message_list} \n")

# Encrypt message
padded_message = []
for i in message_list:
    padded_character = str(ord(i))
    padded_message.append(padded_character)
    # print(padded_character)
print(f"Padded Message: {padded_message} \n")

cipher_text = []
for i in padded_message:
    cipher_character = (int(i) ** public_key_exponent) % n
    cipher_text.append(cipher_character)
print(f"Cipher text :{cipher_text} \n")

decrypted_cipher = []
for i in cipher_text:
    decrypted_value = (i**secret_key_exponent) % n
    decrypted_cipher.append(decrypted_value)

print(f"Decrypted values: {decrypted_cipher} \n")

decrypted_message_list = []
for i in decrypted_cipher:
    normal_character = chr(i)
    decrypted_message_list.append(normal_character)

print(f"Decrypted message list: {decrypted_message_list} \n")

print(f"Decrypted message is: \n")
for i in decrypted_message_list:
    print(i, end="")
print("\n")
