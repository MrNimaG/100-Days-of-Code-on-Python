# import art


# TODO-1: Import and print the logo from art.py when the program starts.
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):


    if encode_or_decode == 'encode':
        cipher_text = ''
        for char in original_text:
            if char in alphabet:
                cipher_text += alphabet[(alphabet.index(char) + shift_amount) % len(alphabet)]
            else:
                cipher_text += char
        print(cipher_text)

    elif encode_or_decode == 'decode':
        decrypt_text = ''
        for char in original_text:
            if char in alphabet:
                decrypt_text += alphabet[(alphabet.index(char) - shift_amount) % len(alphabet)]
            else:
                decrypt_text += char
        print(decrypt_text)
    else:
        print("Wrong Input! try again")







# TODO-3: Can you figure out a way to restart the cipher program?



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
condition_for_loop = True

while condition_for_loop:
    answer = input('Type \'Yes\' if you want to go again. Otherwise type \'No\' \n').lower()
    if answer == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    elif answer == 'no':
        condition_for_loop = False
        print("thank you for using Caesar Ciphering Machine")

