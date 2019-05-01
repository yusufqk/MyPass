#!/usr/bin/env python

import os
import sys
import bcrypt
from time import sleep
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.shortcuts import yes_no_dialog
from prompt_toolkit.shortcuts import message_dialog
from Cryptodome.Cipher import AES
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES, PKCS1_OAEP
from modules.my_aes import aes_encrypt
from modules.pass_check import valid_pass
from modules.rsa_gen import rsa_make
from modules.my_rsa import rsa_encrypt

class MakePass:


    def hash_pass(self,password):

        hash_key = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        with open("hash.txt","wb") as fobj:

            fobj.write(hash_key)


    def setup(self,passwd):

        path = "./Keys"

        if not os.path.exists(path):

            os.makedirs(path)

        else:

            print_formatted_text(HTML('<ansired>[!] Keys folder already exists. Delete it first!</ansired>'))
            sys.exit()


        print_formatted_text(HTML('<seagreen>[*] Generating RSA Keys...</seagreen>'))

        sleep(1)

        rsa_make()
        
        print_formatted_text(HTML('<seagreen>[*] Setting up AES encryption...</seagreen>'))

        aes_encrypt(passwd)

        sleep(1)

        string = "Welcome to MyPass Manager"

        os.system("touch passwords.txt")
        os.system("echo Welcome_to_MyPass > passwords.txt")

        sleep(1)

        rsa_encrypt()

        print_formatted_text(HTML('<skyblue>[*] Setup complete.</skyblue>'))
        


    def __call__(self):


        print_formatted_text(HTML('<seagreen>[*] Starting setup now...</seagreen>'))
        sleep(1)

        while True:

            message_dialog(title="Password Selection",text="Create a strong password.\nAt least 1 number and 1 special character with a length of 16.")
            passwd_1 = input_dialog(title='Password Selection',text='Enter Master Password',password=True)

            if passwd_1 == None:

                sys.exit()

            passwd_2 = input_dialog(title='Password Confirmation',text='Confirm Password', password=True)
           
            if passwd_2 == None:

                sys.exit()

            if passwd_1 == passwd_2:
                
                check = valid_pass(passwd_1)

                if check == True:
                    
                    break

                else:
                    
                    result = yes_no_dialog(title="Error!",text="Your password was not strong enough.\nDo you want to try again?")
                    
                    if result == True:

                        continue

                    else:

                        sys.exit()

            else:

                result = yes_no_dialog(title="Error!",text="Your passwords didn't match.\n Do you want to try again?")

                if result == True:

                    continue

                else:

                    sys.exit()


        self.hash_pass(passwd_1)
        self.setup(passwd_1)
    



if __name__ == "__main__":

    loop = MakePass()

    loop()
    





