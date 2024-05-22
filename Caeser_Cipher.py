import random
import math
alpha =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def func_encrypt(data,shifts):
    encrypt_text = ""
    for letter in data:
        flag = alpha.index(letter)
        new_p = flag + shifts
        encrypt_text += alpha[new_p]
    
    print(f"Encrypted text is = {encrypt_text}")
        
def func_decrypt(data,shifts):
    decrypt_text = ""
    for letter in data:
        flag = alpha.index(letter)
        new_p = flag - shifts
        decrypt_text += alpha[new_p]
        
    print(f"Decrypted text is = {decrypt_text}")
        
shift_amount = int(input("Enter places to be shifted :"))
text = input("Enter the text: ").lower()

choice = input("Enter 'E' for encryption or 'D' for decryption : ").upper()

if choice == 'E':
    func_encrypt(text,shift_amount)
elif choice == 'D':
    func_decrypt(text,shift_amount)
   