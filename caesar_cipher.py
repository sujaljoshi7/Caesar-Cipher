from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keep_running = True


def caesar(text, shift, action):
    output = ""
    if action == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            temp_index = int(alphabet.index(char))
            output += (alphabet[temp_index + int(shift)])
        else:
            output += char
    print(f"The {direction}d text is {output}")


while keep_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    input_text = input("Type your message:\n").lower()
    input_shift = int(input("Type the shift number:\n"))
    input_shift = input_shift % 26
    caesar(input_text, input_shift, direction)
    continue_game = input("Do you want to continue? Type 'yes' to continue or 'no' to exit ").lower()
    if continue_game != "yes":
        keep_running = False

print("Goodbye 👋")
