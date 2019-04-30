#!/usr/bin/env python

from prompt_toolkit import print_formatted_text,HTML
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import prompt
import sys

class Adder:

    def __init__(self,cmd_session):

        self.name = "Adder"
        self.prompt = HTML('MP (<ansired>Adder</ansired>) ≫  ')
        self.cmd_session = cmd_session

    def add_acct(self,acctname,username,passwd,lines):

        new_data = "%s:%s:%s" % (acctname,username,passwd)
        lines.append(new_data)
        print_formatted_text(HTML("<seagreen>[*] Account successfully added.</seagreen>"))
        return new_data

    def run(self,lines):
        
        while True:

            account_name = prompt("Enter account name: ")
            username = prompt("Enter username: ")
            while True:
                password = prompt("Enter account password: ",is_password=True)
                password_chk = prompt("Confirm password: ",is_password=True)
                if password == password_chk:
                    break
                else:
                    print("[!] Passwords did not match. Try again.")
            
            self.add_acct(account_name,username,password,lines)
            break




