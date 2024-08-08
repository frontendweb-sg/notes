class CaeserCipher:
    letters = 'abcdefghijklmnopqrstuvwxyz'

    def encode(self, message: str, shift: int):
        result = ''
        for char in message:
            if char in self.letters:
                pos = self.letters.index(char.lower())
                new_pos = (pos+shift) - 26 if (pos+shift) > 26 else pos+shift
                result += self.letters[new_pos]
            else:
                result += char
        print('You encrypted message is : {}'.format(result))

    def decode(self, message: str, shift: int):
        result = ''
        for char in message:
            pos = self.letters.index(char.lower())  # z-26,shfit - 5
            new_pos = pos - shift
            result += self.letters[new_pos]
        print('You decrypted message is : {}'.format(result))

    @classmethod
    def init(cls):
        type = input("Type 'encode' to encrypt and 'decode' to decrypt: ")
        message = input("Enter your message: ")
        shift = int(input("Type the shift number: "))
        shift = shift % 26
        if type == "encode":
            cls.encode(cls, message, shift)
        else:
            cls.decode(cls, message, shift)


if __name__ == "__main__":
    repeat = True
    while repeat:
        print("Type 'yes' if you want to go again. Otherwize type 'no': ")
        ask = input("")
        if ask == "no" or ask == "NO":
            repeat = False
            print("Goodbye")
            break
        CaeserCipher.init()
