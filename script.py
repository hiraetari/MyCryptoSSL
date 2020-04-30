from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import os


def generate_keypair():
    keyname = input("Please, input keyname: ")
    privKeyFile = open('keys/' + keyname + '.key','wb')
    pubKeyFile = open('keys/' + keyname + '.crt','wb')
    key = RSA.generate(1024, os.urandom)
    privKeyFile.write(key.exportKey())
    pubKeyFile.write(key.publickey().exportKey())
    privKeyFile.close()
    pubKeyFile.close()


command ="";
while command != "exit":
    try:
        command = input("Please, enter command: \n")
        if  command == "keygen":
            generate_keypair()
            continue
        elif command == "sign":
            print("check")
            continue
        elif command == "verify":
            print("check")
            continue
        elif command == "sh_keychain":
            print("check")
            continue
        elif command == "help":
            print("Commands list:\n"
            "keygen -"
            "sign - "
            "verify -"
            "sh_keychain -"
            "help -")
            continue
        elif command == "exit":
            print("See you next time!")
        else:
            print("Unknown command")
    except ValueError:
        print("Syntax error")
