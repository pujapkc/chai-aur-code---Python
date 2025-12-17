alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def encrypt(original_text, shift):
    cipher_text = ""

    for letter in original_text:
        if letter in alphabets:
            shifted_position = alphabets.index(letter) + shift
            shifted_position %= len(alphabets)
            cipher_text += alphabets[shifted_position]
        else:
            cipher_text += letter

    print(f"Your cipher text is: {cipher_text}")


def decrypt(cipher_text, shift):
    original_text = ""

    for letter in cipher_text:
        if letter in alphabets:
            shifted_position = alphabets.index(letter) - shift
            shifted_position %= len(alphabets)
            original_text += alphabets[shifted_position]
        else:
            original_text += letter

    print(f"Your original text is: {original_text}")


while True:
    choice = input(
        "\nType 'encode' to encrypt\n"
        "Type 'decode' to decrypt\n"
        "Type 'exit' to quit\n"
    ).lower()

    if choice == "exit":
        print("Goodbye 👋")
        break

    elif choice == "encode" or choice == "decode":
        text = input("Type your text:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if choice == "encode":
            encrypt(text, shift)
        else:
            decrypt(text, shift)

    else:
        print("Invalid choice, please try again!")
