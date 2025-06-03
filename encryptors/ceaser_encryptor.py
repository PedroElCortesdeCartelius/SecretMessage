from encryptors.encryptor import Encryptor
import random
import string

class ceaser_enc(Encryptor):
    def __init__(self):
        self.shift = 8

    def encrypt(self, message:str):
        alphabet=string.ascii_letters
        shifted=alphabet[self.shift:]+alphabet[:self.shift]
        table=str.maketrans(alphabet, shifted)
        encrypted=f"{message.translate(table)}"
        return encrypted


    def decrypt(self, encrypted:str):
        alphabet=string.ascii_letters
        shifted=alphabet[self.shift:]+alphabet[:self.shift]
        table=str.maketrans(shifted, alphabet)
        decrypted=encrypted.translate(table)
        return decrypted












