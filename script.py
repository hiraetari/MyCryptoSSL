from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import os
import time

def generateKeypair():
    keyname = input("Please, input keyname: ")
    privKeyFile = open('keys/' + keyname + '.key','wb')
    pubKeyFile = open('keys/' + keyname + '.crt','wb')
    key = RSA.generate(1024, os.urandom)
    privKeyFile.write(key.exportKey())
    pubKeyFile.write(key.publickey().exportKey())
    privKeyFile.close()
    pubKeyFile.close()

def getHash(fname):
    hash = SHA256.new()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    return hash

def fileSign():
    keyName = input("Please, input keyname: ")
    privKeyFile = open('keys/' + keyName + '.key','rb')
    key = RSA.importKey(privKeyFile.read())
    fileName = input("Please, input filename: ")
    signature = pkcs1_15.new(key).sign(getHash(fileName))
    sigFile= open('signs/' + str(time.time()) +'.sign','wb')
    sigFile.write(signature)
    privKeyFile.close()
    sigFile.close()

command ="";
while command != "exit":
    try:
        command = input("Please, enter command: \n")
        if  command == "keygen":
            generateKeypair()
            continue
        elif command == "sign":
            fileSign()
        elif command == "verify":
            print("check")
            continue
        elif command == "sh_keychain":
            print("check")
            continue
        elif command == "help":
            print("Commands list:\n"
            "keygen - generate new keypair\n"
            "sign - sign a file\n"
            "verify - verify file\n"
            "sh_keychain - show existing keypairs\n"
            "help - show this list\n")
            continue
        elif command == "exit":
            print("See you next time!")
        else:
            print("Unknown command")
    except ValueError:
        print("Syntax error")
