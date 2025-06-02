import string

from SecretHider.file_handler import FileHandler
from encryptors.ceaser_encryptor import ceaser_enc
from encryptors.encryptor import Encryptor
from encryptors.reverse_encryptor import reverse_enc
from utils.markers import START_MARKER, END_MARKER
import os

class SecretManager:
    def __init__(self, encryptor):
        self.encryptor = encryptor
        self.file_handler = FileHandler()
        self.marker_start = START_MARKER
        self.marker_end = END_MARKER
    def hide(self, path:str, text:str):
        encrypted=self.encryptor.encrypt(text)
        full_content = self.file_handler.read_file(path)
        new_content = f"{full_content}\n{self.marker_start}\n{encrypted}\n{self.marker_end}\n"
        self.file_handler.write_file(path, new_content)
        print("The secret is successfully hidden")

    def reveal(self, path:str):
        content=self.file_handler.read_file(path)
        start=content.find(self.marker_start)
        end=content.find(END_MARKER)
        encrypted = content[start + len(self.marker_start):end].strip()
        decrypted = self.encryptor.decrypt(encrypted)
        return decrypted
    def delete(self, path:str):
        content=self.file_handler.read_file(path)
        start = content.find(self.marker_start)
        end = content.find(self.marker_end)
        end += len(self.marker_end)
        new_content = content[:start].rstrip() + '\n' + content[end:].lstrip()
        self.file_handler.write_file(path, new_content)
        print("Secret message deleted successfully.")


















