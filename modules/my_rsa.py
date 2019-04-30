#!/usr/bin/env python

from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_OAEP
from time import sleep

def rsa_encrypt():

    with open("./passwords.txt","rb") as fobj:
        data = fobj.read()


    with open("./Keys/public.pem","rb") as fobj1:
        public_key = fobj1.read()

    public_key = RSA.import_key(public_key)

    cipher_rsa = PKCS1_OAEP.new(public_key)
    session = cipher_rsa.encrypt(data)

    with open("./passwords.txt","wb") as fobj2:
        fobj2.write(session)



def rsa_decrypt(private_key):

    
    with open("./passwords.txt","rb") as fobj:
        data = fobj.read()
        
    private_key = RSA.import_key(private_key)

    cipher_rsa = PKCS1_OAEP.new(private_key)
    session = cipher_rsa.decrypt(data)

    session = session.decode("utf-8") 
    
    #with open("./passwords.txt","wb") as fobj2:
    #    fobj2.write(session)

    return session.splitlines()




