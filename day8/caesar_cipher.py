"""
Caesar Cipher
-------------
Encrypts or decrypts a message using the Caesar cipher algorithm.

Rules:
- Encode: shift each letter forward by shift amount
- Decode: shift each letter backward by shift amount
- Wrap-around using % 26 — no manual boundary check needed
- Non-alphabet characters (spaces, numbers, symbols) kept unchanged
- Play again loop using while + boolean flag
"""

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(direction, text, shift):
    output_text = list(text)
    for position, letter in enumerate(text):
        if letter not in alphabets:
            output_text[position] = letter
        else:
            if direction == 'encode':
                shifted_index = (alphabets.index(letter) + shift) % 26
            if direction == 'decode':
                shifted_index = (alphabets.index(letter) - shift) % 26
            output_text[position] = alphabets[shifted_index]
    print(f"output text is: {''.join(output_text)}")

print(logo)

repeat = True
while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    play_again = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n").lower()
    if play_again == 'no':
        repeat = False