# Encryption: Mã hóa (encode)
# Decryption: Giải mã (decode)
import Caesar_art
print(Caesar_art.logo)

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(text ,shift):
    text_len = len(text)
    res_text = ''

    for i in range(0,text_len):

        if text[i] in alphabet:
            find = shift + alphabet.index(text[i])
            res_text+=alphabet[find%26]

        else:
            res_text+=text[i]

    print(str(res_text))

def decrytion(text, shift):
    text_len = len(text)
    res_text = ''

    for i in range(0, text_len):

        if text[i] in alphabet:
            find = alphabet.index(text[i])-shift
            res_text += alphabet[find%26]

        else:
            res_text += text[i]

    print(str(res_text))

def caesar(text, shift,direction):
    if direction == 'encode':
        encryption(text, shift)
    else:
        decrytion(text, shift)
ask="yes"

while ask=="yes":
    direction = input("Type 'encode' to encryption or 'decode' to decryption: ")
    text = input("Type you message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar(text,shift,direction)

    ask = input("Do you want to continue? Yes or no? ").lower()





