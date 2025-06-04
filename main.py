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
while True:
    path=input("Enter the file path: ").strip()
    if not os.path.exists(path):
        print("File does not exist")
        exit()
    print("What do you want to do with the secret? \n1:Hide \n2:Reveal \n3:Delete")
    option=input("Enter the number:")
    if option=="1":
        message=input("Enter the secret(enter only latin letters): ")
        encryptor=input("Which encryptor would you like to use? \n1:Ceaser encryptor \n2:Reverse alphabet encryptor \nEnter the number:")
        if encryptor=="1":
            SecretManager(ceaser_enc()).hide(path, message)
        elif encryptor=="2":
            SecretManager(reverse_enc()).hide(path, message)
        else:
            print("There is no such option")
    if option=="2":
        encryptor=input("Which encryptor is used?: \n1:Ceaser encryptor \n2:Reverse alphabet encryptor")
        if encryptor=="1":
            decrypted_secret = SecretManager(ceaser_enc()).reveal(path)
            print("The secret is: " , decrypted_secret)
        elif encryptor=="2":
            decrypted_secret = SecretManager(reverse_enc()).reveal(path)
            print(decrypted_secret)
        else:
            print("there is no such option")

    elif option=="3":
        SecretManager(None).delete(path)
    else:
        print("there is no such option")
    cont = input("Do you want to continue? \n1:Yes \n2:No  \n")
    if cont!="1":
        exit()











