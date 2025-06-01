from encryptors.encryptor import Encryptor
import string

class reverse_enc(Encryptor):
    def encrypt(self, message:str):
        alphabet=string.ascii_letters
        rev_alphabet=alphabet[::-1]
        table=str.maketrans(alphabet, rev_alphabet)
        rev_encrypted=message.translate(table)
        return rev_encrypted\


    def decrypt(self, encrypted:str):
        alphabet=string.ascii_letters
        rev_alphabet=alphabet[::-1]
        table=str.maketrans(rev_alphabet, alphabet)
        rev_encrypted=encrypted.translate(table)
        return rev_encrypted








