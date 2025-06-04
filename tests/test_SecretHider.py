import unittest
import os
from SecretHider.file_handler import FileHandler
from SecretHider.file_vault import SecretManager
from encryptors import ceaser_encryptor
from unittest.mock import MagicMock
from SecretHider.invisible_text import invisible, visible
from encryptors.ceaser_encryptor import ceaser_enc


class TestSecretHider(unittest.TestCase):
    def setUp(self):
        self.encryptor = ceaser_enc()
        self.manager = SecretManager(self.encryptor)
        self.manager.file_handler = MagicMock()

    def test_read_write(self):
        self.file_handler = FileHandler()
        self.test_file = "test_file.txt"
        content = "¿Qué le dijo el semáforo al carro? \n¡No mires, que me estoy cambiando!"
        self.file_handler.write_file(self.test_file, content)
        result = self.file_handler.read_file(self.test_file)
        self.assertEqual(result, content)

    def test_hide(self):
        self.manager.file_handler.read_file.return_value = "appple"
        self.manager.hide("file.txt", "secret")
        self.manager.file_handler.write_file.assert_called()

    def test_reveal(self):
        self.manager.file_handler.read_file.return_value = "a parrot"
        result = self.manager.reveal("file.txt")
        self.manager.file_handler.read_file.assert_called()
        self.assertIsInstance(result, str)

    def test_delete(self):
        self.manager.file_handler.read_file.return_value = "Cristiano Ronaldo"
        self.manager.delete("file.txt")
        self.manager.file_handler.write_file.assert_called()


    def test_invisible_visible(self):
        message = "skibidiohiorizzler"
        hidden = invisible(message)
        revealed = visible(hidden)
        self.assertEqual(revealed, message)



if __name__ == '__main__':
    unittest.main()




