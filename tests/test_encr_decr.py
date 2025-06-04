import unittest
from encryptors.ceaser_encryptor import ceaser_enc
from encryptors.reverse_encryptor import reverse_enc
from SecretHider.invisible_text import invisible, visible


class TestEncryptors(unittest.TestCase):
    def test_ceaser_encrypt_decrypt(self):
        enc=ceaser_enc()
        message ="Hydrochlorofluorocarbon"
        encrypted = enc.encrypt(message)
        decrypted = enc.decrypt(encrypted)
        self.assertEqual(decrypted, message)

    def test_reverse_encrypt_decrypt(self):
        enc=reverse_enc()
        message = "Supercalifragilisticexpialidocious"
        encrypted= enc.encrypt(message)
        decrypted=enc.decrypt(encrypted)
        self.assertEqual(decrypted, message)




if __name__ == '__main__':
    unittest.main()
