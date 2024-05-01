#!/usr/bin/env python
# coding: utf-8

# In[1]:


alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_key)%26
            cipher_text+=alphabet[new_position]
        else:
            cipher_text+=char
    print(f"Here is the encrypted text {cipher_text}")
    
def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position-shift_key)%26
            plain_text+=alphabet[new_position]
        else:
            plain_text+=char
    print(f"Here is the decrypted text {plain_text}")

want_to_end=False
while not want_to_end:
    choice=input("Type 'encrypt' for encryption,Type 'decrypt' for decryption:").lower()
    message=input("Type your message:")
    shift_number=int(input("Enter shift number:"))

    if choice=='encrypt':
        encryption(plain_text=message,shift_key=shift_number)
    elif choice=='decrypt':
        decryption(cipher_text=message,shift_key=shift_number)
    play_again=input("Want to play again('yes','no'):\n")
    if play_again=='no':
        want_to_end=True
        print("Have a nice day! bye..")
    


# In[ ]:




