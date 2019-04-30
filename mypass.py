#!/usr/bin/env python

from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text,HTML
from prompt_toolkit import PromptSession
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.shortcuts import input_dialog
from terminaltables import AsciiTable
from terminaltables import SingleTable
from modules.my_rsa import rsa_encrypt, rsa_decrypt
from modules.my_aes import aes_encrypt,aes_decrypt
from modules.art import one,two,third,fourth
from actions.adder import Adder
from actions.deleter import Deleter
from actions.modifier import Modifier
from actions.viewer import Viewer
import shlex
import time
import bcrypt
import getpass
import sys
import os


def sign_in():

    passwd = prompt("Enter Master Password: ",is_password=True)

    with open("hash.txt","rb") as fobj:

        hashed_pass = fobj.read()

    if (hashed_pass == bcrypt.hashpw(passwd.encode("utf-8"),hashed_pass)):
        return passwd,True

    else:
        return passwd,False


def bottom_toolbar(lines):
    
    count = len(lines)

    accounts = "Accounts: %d   " % count
    date_time = str(time.ctime())
    
    date_items = shlex.split(date_time)

    del date_items[3]
    date_wanted = " ".join(date_items)

    statement = accounts + date_wanted

    return HTML("%s" % statement)



class MyPass:

    def __init__(self,data):

        self.data = data

        self.table_help = [
                ["Command","Description"],
                ["Adder", "Add an account and its password to the list"],
                ["Deleter", "Delete an existing account and the password from the list"],
                ["Modifier", "Modify the username and/or password from the list"],
                ["Viewer", "Extract the user and/or password to sign into an account"],
                ["Run", "Executes the module that is being used"],
                ["Exit", "Logout from MyPass"]
                ]


        self.passwords = self.data

        self.cmd_session = PromptSession(
                "MP >> ",
                complete_while_typing=True
                )
        
        self.actions = [
                Adder(self.cmd_session),
                Deleter(self.cmd_session),
                Modifier(self.cmd_session),
                Viewer(self.cmd_session),
        ]
        self.cmd_session.completer = self.completer = WordCompleter([mod.name for mod in self.actions] + ["exit","help","run"] ,ignore_case=True)
        self.current_module = self


    
    def list_accts(self):

        string = ""

        for i in range(len(self.passwords)):
            items = self.passwords[i].split(":")
            acct_name = items[0]
            string += acct_name+" "

        table_instance = SingleTable([[string]], 'Accounts')
        print(table_instance.table)
        print("")
    


    def switch_module(self,result):


        for mod in self.actions:

            if result == mod.name:

                self.cmd_session.message = mod.prompt
                self.current_module = mod

                return True

        return False



    def exit(self):

        with open("passwords.txt","w") as fobj:
            for i in range(len(self.passwords)):
                self.passwords[i] = str(self.passwords[i])
                fobj.write(self.passwords[i]+"\n")

        rsa_encrypt()



    def pass_terminal(self):


        while True:

            text = self.cmd_session.prompt(bottom_toolbar=bottom_toolbar(self.passwords))
            
            if text == "exit":
                self.exit()
                sys.exit()
            else:
                switch_result = self.switch_module(text)
                if switch_result == False:
                    if text.lower() == "run":
                        self.current_module.run(self.passwords)
                    elif text.lower() == "help":
                        table = AsciiTable(self.table_help)
                        table.inner_row_border = True
                        print(table.table)
                        print("")
                    elif text.lower() == "list":
                        self.list_accts()
                    else:
                        print("[!] Command not found.")
                else:
                    continue




if __name__ == "__main__":

    os.system("clear")

    while True:

        passwd,check = sign_in()

        if passwd.lower() == "exit":
            sys.exit()
        
        if check == False:
            
            print("[!] Wrong password. Try again.")
            continue

        else:
            break

    private_key = aes_decrypt(passwd)
    data = rsa_decrypt(private_key)
    
    time.sleep(1)

    print("")
    print(two)
    print("")
    #print(one)
    #print("")
    print("")

    start = MyPass(data)

    run_in_terminal(start.pass_terminal())


