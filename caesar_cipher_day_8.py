print('''                                                                  
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
              88  ''')

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
direction=input("Type Encode to Encript, Type Decode to Decript\n").lower()
text=input("Type Your Message\n").lower()
shift=int(input("Type the Shift number"))

# def encrypt(original_text,shift_amount):
#     cipher_text=""
#     for letter in original_text:
#         shifted_position=alphabet.index(letter)+shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text+=alphabet[shifted_position]
#     print(f"here is the encoded result: {cipher_text}")
# encrypt(original_text=text,shift_amount=shift)


# def decrypt(original_text,shift_amount):
#     output_text=""
#     for letter in original_text:
#         shifted_position=alphabet.index(letter)-shift_amount
#         shifted_position %= len(alphabet)
#         output_text+=alphabet[shifted_position]
#     print(f"here is the encoded result: {output_text}")
# decrypt(original_text=text,shift_amount=shift)

def caesar(original_text,shift_amount,encode_or_decode):
    output_text=""
    if encode_or_decode=="decode":
        shift_amount*= -1
    for letter in original_text:
        if letter not in alphabet:
             output_text+=letter
        else:  
            shifted_position=alphabet.index(letter)+shift_amount
            shifted_position %= len(alphabet)
            output_text+=alphabet[shifted_position]
    print(f"here is the {encode_or_decode}d result: {output_text}")
caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("\nDo you want to restart? Type 'yes' to go again, or 'no' to quit:\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")


# should_continue=True
# while should_continue:
    
#     direction=input("Type Encode to Encript, Type Decode to Decript\n").lower()
#     text=input("Type Your Message\n").lower()
#     shift=int(input("Type the Shift number"))
#     caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)
#     restart=input("Type 'Yes'if you want to go again, otherwise type'No'\n").lower()
#     if restart=="no":
#         should_continue=False
#         print("GoodBye")

