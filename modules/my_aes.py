#!/usr/bin/env python

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from time import sleep


def aes_encrypt(key):

    key = key.encode("utf-8")

    with open("./Keys/private.pem","rb") as inputs:
        data = inputs.read()

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    with open("./Keys/private.pem", "wb") as file_out:
        [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]


def aes_decrypt(key):

    key = key.encode("utf-8")

    with open("./Keys/private.pem", "rb") as file_in:
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    return data
