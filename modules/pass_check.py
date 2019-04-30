#!/usr/bin/python3



def valid_pass(password):

    special_char = "!@#$%^&*()<>?"
    numbers = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    
    password = password.lower()

    count_char = 0
    count_num = 0
    count_letters = 0

    for i in range(len(password)):

        if password[i] in special_char:

            count_char += 1

        if password[i] in numbers:

            count_num += 1

        if password[i] in letters:

            count_letters += 1


    if count_char > 0 and count_num > 0 and count_letters > 0 and len(password) == 16:

        return True

    else:

        return False


