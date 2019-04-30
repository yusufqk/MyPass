#!/usr/bin/env python

from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import prompt
from actions.count_pass import count
import sys
import pyperclip


class Viewer:

    def __init__(self,cmd_session):

        self.name = "Viewer"
        self.prompt = HTML('MP (<ansired>Viewer</ansired>) ≫  ')
        self.cmd_session = cmd_session


    def view(self,account,lines):

        for i in range(len(lines)):
            lines[i] = str(lines[i])
            items = lines[i].split(":")
            acct_item = items[0]
            if acct_item == account:
                passwd = items[2]
                pyperclip.copy(passwd)
                acct_passwd = pyperclip.paste()
                count()
                pyperclip.copy("WUBBA LUBBA DUB DUBS!!!")
                clearing = pyperclip.paste()
                break


    def run(self,lines):

        while True:
            account = prompt("Enter account name: ")
            self.view(account,lines)
            break
       
