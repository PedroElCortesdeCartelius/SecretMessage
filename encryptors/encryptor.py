from abc import ABC, abstractmethod

class Encryptor(ABC):
    @abstractmethod
    def encrypt(self, str):
        pass
    def decrypt(self,str):
        pass





