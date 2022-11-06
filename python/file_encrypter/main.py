"""
Read the README for information on what this project is.

"""

# dependencies
from cryptography.fernet import Fernet
import os
import hashlib
import pathlib



# TODO: fix key not being safe enough, use different algorithm perhaps



def encrypt(filepath,key):
    """
    This function decrypts the file
    """


    #encrypting the file itself
    fernet = Fernet(key)
    with open(filepath, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filepath, "wb") as encrypted_file:
        encrypted_file.write(encrypted)





def decrypt(filepath,key):
    """
    This function encrypts the file
    """


    fernet = Fernet(key)
    with open(filepath, "rb") as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(filepath, "wb") as file:
        file.write(decrypted)








def init_encrypt():
    """
    This function provides all the other funcionality required to encrypt the file
    """

    file_path = input("Please paste the file path in here (full path to the file itself, NOT the folder in which the file is!\n")
    path = pathlib.Path(file_path)

    if not os.path.exists(file_path):
        print("file was not found.")
        quit()

    here = pathlib.Path(__file__).parent
    hash_folder = here / "key_hashes"
    key = input("Please input a key:\n")


    # save a hashed value of the key in a file to prevent issues when decrypting files
    encoded_key = key.encode()
    hashed_key = hashlib.sha256(encoded_key).hexdigest()

    filename = path.stem
    
    path_to_hash = hash_folder / f"{filename}.keyhash"

    with open(path_to_hash,"w") as file:
        file.write(hashed_key)

    print("Starting encryption process !")

    #encrypt(file_path,key)#actually encrypting the file
    print("encryption process successfull")






def init_decrypt():

    file_path = input("Please paste the file path in here (full path to the file itself, NOT the folder in which the file is!\n")
    path = pathlib.Path(file_path)

    if not os.path.exists(file_path):
        print("file was not found.")
        quit()

    here = pathlib.Path(__file__).parent
    hash_folder = here / "key_hashes"
    key = input("Please input a key:\n")


    # save a hashed value of the key in a file to prevent issues when decrypting files
    encoded_key = key.encode()
    hashed_key = hashlib.sha256(encoded_key).hexdigest()

    filename = path.stem
    
    path_to_hash = hash_folder / f"{filename}.keyhash"

    with open(path_to_hash,"r") as file:
        actual_hash = file.readline()

    if actual_hash != hashed_key:
        print("key is not correct")
        quit()
    else:
        print("key correct, starting decryption process !")


    #decrypt(file_path,key)# actually decrypting the file
    print("decryption process successfull")






def main():
    """
    main function
    """

    choice = input("Encrypt file (1) or decrypt file(2):\n")

    try:
        choice = int(choice)
    except ValueError:
        print("input is not valid.")
        quit()

    if choice == 1:
        init_encrypt()

    elif choice == 2:
        init_decrypt()


if __name__ == "__main__":
    main()



