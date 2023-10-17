def main():
    user_choice = get_response()
    shift_number = get_shift_number()
    message = get_message()
    result = " "

    if user_choice == "encode":
        encryptor(message, shift_number, result)
    elif user_choice == "decode":
        decryptor(message, shift_number, result)


def get_response():
    while True:
        try:
            choice = input("Type 'encode' to encrypt, type 'decode' to decrypt ")
            if choice == "encode" or choice == "decode":
                break
            else:
                pass
        except ValueError:
            pass
    return choice


def get_shift_number():
    while True:
        try:
            choice = int(input("Type shift number "))
            break
        except ValueError:
            print("Please provide number")
            pass
    return choice


def get_message():
    while True:
        try:
            choice = input("Type message: ")
            break
        except ValueError:
            print("Please provide message(text)")
            pass
    return choice


def decryptor(message, shift_number, result):
    temp = list(message)
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            result += chr((ord(char) + shift_number - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift_number - 97) % 26 + 97)
    print(result)
    return result


def encryptor(message, shift_number, result):
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            result += chr((ord(char) - shift_number - 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift_number - 97) % 26 + 97)
    print(result)
    return result


if __name__ == "__main__":
    main()
