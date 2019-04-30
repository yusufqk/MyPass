#!/usr/bin/env python

from prompt_toolkit import print_formatted_text
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import prompt
import sys


class Deleter:

    def __init__(self,cmd_session):

        self.name = "Deleter"
        self.prompt = HTML('MP (<ansired>Deleter</ansired>) ≫  ')
        self.cmd_session = cmd_session


    def del_acct(self,acct,lines):

        for i in range(len(lines)):
            entry_list = lines[i].split(":")
            if entry_list[0] == acct:
                del lines[i]
                return lines
                               

    def run(self,lines):
        
        while True:

            account_name = prompt("Enter account name: ")
            result = self.del_acct(account_name,lines)
            print_formatted_text(HTML("<seagreen>[*] Account successfully deleted.</seagreen>"))
            break

