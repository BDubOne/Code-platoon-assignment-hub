def caesar_cipher(string, shift_amount):
    shift_amount = shift_amount % 26

    caesar_salad = []

    for char in string:
        if "A" <= char <= 'Z':

            shifted = (ord(char) - ord('A') + shift_amount) % 26
            caesar_salad.append(chr(shifted + ord('A')))

        elif 'a' <= char <= 'z':
            shifted = (ord(char) - ord('a') + shift_amount) % 26
            caesar_salad.append(chr(shifted + ord('a')))
        else:
            caesar_salad.append(char)

    return ''.join(caesar_salad)

