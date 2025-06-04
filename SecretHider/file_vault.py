from SecretHider.file_handler import FileHandler
from encryptors.ceaser_encryptor import ceaser_enc
from encryptors.encryptor import Encryptor
from encryptors.reverse_encryptor import reverse_enc
from utils.markers import START_MARKER, END_MARKER, START_MARKER2, END_MARKER2
from SecretHider.invisible_text import invisible
from SecretHider.invisible_text import visible
import os
import string

class SecretManager:
    def __init__(self, encryptor):
        self.encryptor = encryptor
        self.file_handler = FileHandler()
        self.marker_start = START_MARKER
        self.marker_end = END_MARKER
    def hide(self, path:str, text:str):
        encrypted=self.encryptor.encrypt(text)
        full_content = self.file_handler.read_file(path)
        new_content = f"{full_content}\n{invisible(self.marker_start)}\n{invisible(encrypted)}\n{invisible(self.marker_end)}\n"
        self.file_handler.write_file(path, new_content)
        print("Secret successfully hidden")

    def reveal(self, path:str):
        content=self.file_handler.read_file(path)
        start=content.find(self.marker_start)
        end=content.find(END_MARKER)
        encrypted = content[start + len(self.marker_start):end].strip()
        encrypted=visible(encrypted)
        start2 = encrypted.find(START_MARKER2)
        end2 = encrypted.find(END_MARKER2, start2)
        encrypted = encrypted[start2 + len(START_MARKER2):end2].strip()
        decrypted = self.encryptor.decrypt(encrypted)
        return decrypted

    def delete(self, path:str):
        content=self.file_handler.read_file(path)
        content=visible(content)
        start = content.find(self.marker_start)
        end = content.find(self.marker_end)
        end += len(self.marker_end)
        new_content = content[:start].rstrip() + '\n' + content[end:].lstrip()
        self.file_handler.write_file(path, new_content)
        print("Secret message deleted successfully.")




















