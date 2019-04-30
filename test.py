#!/usr/bin/env python

from __future__ import unicode_literals
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
from modules.art import one,two,third,fourth
from time import sleep
import sys

def tester(func):
    func._zak = True
    return func


class TestNum:

    def __init__(self,fn):

        self.fn = fn
        self.nums = []
        #self.name = ""
    @tester
    def Yuyu(self):
        
        name = "Yusuf"
        return name

    def __call__(self):

        while True:

            result = self.fn()
            self.nums.append(result)
            print(self.nums)


#@TestNum
def get_num():

    input_num = input("Give me a number: ")
    if input_num == "exit":
        sys.exit()
    return input_num


for methodname in dir(TestNum):

    #print(methodname)

    method = getattr(TestNum, methodname)
    print(method)
    #if hasattr(method, "_zak"):
    #    print(str(method) + "Yooo")



#test = TestNum(get_num)
#result = test.Yuyu._zak
#print(result)

#print("")
#print(dir(TestNum))
#get_num()






















"""

table_data = [
    ['Heading1', 'Heading2'],
    ['row1 column1', 'row1 column2'],
    ['row2 column1', 'row2 column2'],
    ['row3 column1', 'row3 column2']
]
table = AsciiTable(table_data)


class NumberValidator(Validator):
    def validate(self, document):
        text = document.text

        if text and not text.isdigit():
            i = 0

            # Get index of fist non numeric character.
            # We want to move the cursor here.
            for i, c in enumerate(text):
                if not c.isdigit():
                    break

            raise ValidationError(message='This input contains non-numeric characters',
                                  cursor_position=i)


bindings = KeyBindings()

@bindings.add('c-t')
def _(event):
    " Say 'hello' when `c-t` is pressed. "
    def print_hello():
        print('hello world')
    run_in_terminal(print_hello)

@bindings.add('c-x')
def _(event):
    " Exit when `c-x` is pressed. "
    event.app.exit()
    

#text = prompt('> ', key_bindings=bindings)
#print('You said: %s' % text)


print
print(fourth)
print("")
print(one)
print("")

style = Style.from_dict({
    # User input (default text).
    '':          '#ff0066',

    # Prompt.
    'username': '#884444',
    'at':       '#00aa00',
    'colon':    '#0000aa',
    'pound':    '#00aa00',
    'host':     '#00ffff bg:#444400',
    'path':     'ansicyan underline',
})

message = [
    ('class:username', 'john'),
    ('class:at',       '@'),
    ('class:host',     'localhost'),
    ('class:colon',    ':'),
    ('class:path',     '/user/john'),
    ('class:pound',    '# '),
]


option_completer = WordCompleter(["Adder", "Aeleter","Adifier","Viewer"])

text = prompt(message, key_bindings=bindings, completer=option_completer, complete_while_typing=True,style=style)

print(table.table)


#number = int(prompt('Give a number: ', validator=NumberValidator()))



#text = input_dialog(title='Input dialog example',text='Please type your name:')
#text1 = input_dialog(title='Input dialog example',text='Please type your name again:')
#print(text,text1)
"""


















