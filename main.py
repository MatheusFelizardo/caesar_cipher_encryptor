alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    new_text = []
    index = 0
    for letter in text:  #civilization
        transcripted = False
        while not transcripted:
            alphabetLetter = alphabet[index]
            alphabetSize = len(alphabet)
            if letter == alphabetLetter:
                position = index + shift
                if (position >= alphabetSize):
                    new_text.append(alphabet[position - alphabetSize])
                else:
                    new_text.append(alphabet[position])
                index = 0
                transcripted = True
            else:
                index += 1
    print(f"The encoded text is {''.join(new_text)}")


def decrypt(text, shift):
    new_text = []
    index = 0
    for letter in text:
        transcripted = False
        while not transcripted:
            alphabetLetter = alphabet[index]
            alphabetSize = len(alphabet)
            if letter == alphabetLetter:
                position = index - shift
                if (position < 0):
                    new_text.append(alphabet[alphabetSize - (-position)])
                else:
                    new_text.append(alphabet[position])
                index = 0
                transcripted = True
            else:
                index += 1
    print(f"The encoded text is {''.join(new_text)}")


if shift > 26:
    shift = shift % 26
if direction == 'encode':
    encrypt(text, shift)
else:
    decrypt(text, shift)
