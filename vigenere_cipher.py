# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 13:34:16 2021

@author: Mustafa

Title: Vigenere Cipher 
"""

import collections
import random
import string


# function to encrypt single character
def caeser(text, shift):
    deque = collections.deque(string.ascii_lowercase)
    deque.rotate(shift)
    deque = ''.join(list(deque))
    return text.translate(str.maketrans(string.ascii_lowercase, deque))

# function to decrypt single character
def caeserDecrypt(text, shift):
    deque = collections.deque(string.ascii_lowercase)
    deque.rotate(26 - shift)
    deque = ''.join(list(deque))
    return text.translate(str.maketrans(string.ascii_lowercase, deque))

# function to implement Vigenere Cipher, encrypt the plain text
def vigenere(text, key):
    text = [i for i in text]
    try:
        encrypted = [caeser(text[i], key[i]) for i in range(len(text))]
        return ''.join(encrypted)
    except IndexError:
        raise IndexError("Key is shorter than message")

# function to generate random keys
def keys(text):
    keys = []
    for i in range(len(text)):
        x = random.randint(0,26)
        keys.append(x)
    print(keys)    
    return keys

# function to decrypt the ciphered text
def decrypt(text, key):
     text = [i for i in text]
     try:
         decrypt = [caeserDecrypt(text[i], key[i]) for i in range(len(text))]
         return ''.join(decrypt)
     except IndexError:
        raise IndexError("Key is shorter than message")
         
     
def main():
    text = input("Enter the text you would like to use: ")
    text.lower()
    key = keys(text)
    encrypted_text =  vigenere(text, key)
    print("Your encrypted text is:\n",encrypted_text)
    decrypted_text = decrypt(encrypted_text, key)
    print("Your decrypted text is:\n",decrypted_text)
        
    
main()
        