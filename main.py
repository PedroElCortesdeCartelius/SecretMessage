from SecretHider.file_handler import FileHandler
from SecretHider.file_vault import SecretManager
from encryptors.ceaser_encryptor import ceaser_enc
from encryptors.encryptor import Encryptor
from encryptors.reverse_encryptor import reverse_enc
from utils.markers import START_MARKER, END_MARKER
from SecretHider.invisible_text import invisible
from SecretHider.invisible_text import visible
import os
import string

print("                                       𝕊𝕖𝕔𝕣𝕖𝕥𝕖𝕄𝕖𝕤𝕤𝕒𝕘𝕖                                    ")
path=input("Enter the file path").strip()
print("What do you want to do with the secret? \n1:Hide \n2:Reveal \n3:Delete")
option=input("Enter the number:")
if option=="1":
    message=input("Enter the secret: ")
    encryptor=input("Which encryptor would you like to use? \n1:Ceaser encryptor \n2:Reverse alphabet encryptor \nEnter the number:")
    if encryptor=="1":
        #inv_message=(invisible(message))
        SecretManager(ceaser_enc()).hide(path, message)


    if encryptor=="2":
        inv_message = invisible(message)
        SecretManager(ceaser_enc()).hide(path, inv_message)
if option=="2":
    decrypted_secret = SecretManager(ceaser_enc()).reveal(path)
    print(decrypted_secret)







