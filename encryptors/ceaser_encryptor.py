from encryptors.encryptor import Encryptor
import random
import string

class ceaser_enc(Encryptor):
    def __init__(self):
        self.shift = random.randint(1, 10)

    def encrypt(self, message:str):
        alphabet=string.ascii_letters
        shifted=alphabet[self.shift:]+alphabet[:self.shift]
        table=str.maketrans(alphabet, shifted)
        encrypted=f"{self.shift}{message.translate(table)}"
        return encrypted


    def decrypt(self, encrypted:str):
        alphabet=string.ascii_letters
        shift=int(encrypted[0])
        encrypted_body=encrypted[1:]
        shifted=alphabet[shift:]+alphabet[:shift]
        table=str.maketrans(shifted, alphabet)
        decrypted=encrypted_body.translate(table)
        return decrypted











