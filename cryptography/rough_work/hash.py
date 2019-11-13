
import hashlib 
  
# initializing string 
str = "GeeksforGeeks"
  
# encoding GeeksforGeeks using encode() 
# then sending to SHA256() 
result = hashlib.sha256(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA256 is : ") 
# print(result.hexdigest()) 
hex_val = result.hexdigest()
print(hex_val)

print ("\r")

i = int(hex_val, 16)
print(f'The decimal equivalent is: {i}')

exp = i * 78945

print(exp)
