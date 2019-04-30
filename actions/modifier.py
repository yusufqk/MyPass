#!/usr/bin/env python


from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import prompt,print_formatted_text
import sys
import shlex


class Modifier:

    def __init__(self,cmd_session):

        self.name = "Modifier"
        self.prompt = HTML('MP (<ansired>Modifier</ansired>) ≫  ')
        self.cmd_session = cmd_session


    def mod_acct(self,account,username,password,lines):

        new_entry = "%s:%s:%s" % (account,username,password)

        for i in range(len(lines)):
            items = lines[i].split(":")
            acct_item_name = items[0]
            if acct_item_name.lower() == account.lower():
                lines[i] = new_entry
                return lines


    def run(self,lines):

        while True:
            account = prompt("Enter account name: ")
            username = prompt("Enter username: ")
            while True:
                password = prompt("Enter account password: ",is_password=True)
                password_chk = prompt("Confirm password: ",is_password=True)
                if password == password_chk:
                    break
                else:
                    print("[!] Passwords did not match. Try again.")

            self.mod_acct(account,username,password,lines)
            print_formatted_text(HTML("<seagreen>[*] Account successfully modified.</seagreen>"))
            break
       
