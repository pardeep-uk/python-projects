alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
          'z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x',
          'y','z']

direction = input("The 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()

shift = int(input("Type shift number:\n"))

def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction == "decode":
            shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"the {cipher_direction}d text is {end_text}")        
        
  
caesar(text,shift,direction)
    

# def encrypt(plain_text,shift_amount):
#     cipher_text=[]
#     for letter in plain_text:
#         next_letter_index = alphabet.index(letter) + shift_amount
#         cipher_text += alphabet[next_letter_index]
#     return ''.join(cipher_text)

# def decrypt(plain_text,shift_amount):
#     cipher_text=[]
#     for letter in plain_text:
#         next_letter_index = alphabet.index(letter) - shift_amount
#         cipher_text += alphabet[next_letter_index]
#     return ''.join(cipher_text)
        
# if direction == 'encode':
#     print(encrypt(text,shift))
# elif direction == 'decode':
#     print(decrypt(text,shift))
    