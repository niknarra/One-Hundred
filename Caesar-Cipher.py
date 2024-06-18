# Day 8 - Jun 18 '24
# Caesar Cipher with Encryption and Decryption Functions

logo=r'''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encodeDecode(method,msg,shift):
    outputMsg = ''
    for char in msg:
        index = alphabet.index(char)
        if method == 'encode':
           outputMsg +=(alphabet[(index + shift) % 26])
        else:
            outputMsg +=(alphabet[(index - shift) % 26])
    print(f"Here is the {method}d message: {outputMsg}")

# def encodeFunc(msg,shift):
#     encodedMsg = ''
#     for char in msg:
#         index = alphabet.index(char)
#         encodedMsg+=(alphabet[(index + shift) % 26])       
#     return encodedMsg

# def decodeFunc(msg,shift):
#     decodedMsg = ''
#     for char in msg:
#         index = alphabet.index(char)
#         decodedMsg+=(alphabet[(index - shift) % 26])  
#     return decodedMsg
    
def Cipher():
    print(logo)

    mode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    
    encodeDecode(mode,message,shift)

    # if mode == 'encode':
    #     print(f"Here's the encoded result: {encodeDecode(mode,message,shift)}")
    # elif mode == 'decode':
    #     print(f"Here's the decoded result: {encodeDecode(mode,message,shift)}")
    # else:
    #     print("Please select only between encode and decode.")
    
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if again == 'yes':
        Cipher()
    else:
        print("Goodbye")

Cipher()

