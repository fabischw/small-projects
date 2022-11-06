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
    with open(filepath, "rb") as file:#reading data
        original = file.read()
    encrypted = fernet.encrypt(original)#encrypting data
    with open(filepath, "wb") as encrypted_file:#writing the data again
        encrypted_file.write(encrypted)





def decrypt(filepath,key):
    """
    This function encrypts the file
    """


    fernet = Fernet(key)
    with open(filepath, "rb") as enc_file:#reading data
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)#decrypting data
    with open(filepath, "wb") as file:#writing the data again
        file.write(decrypted)








def init_encrypt():
    """
    This function provides all the other funcionality required to encrypt the file
    """

    #getting the file path
    file_path = input("Please paste the file path in here (full path to the file itself, NOT the folder in which the file is!\n")
    path = pathlib.Path(file_path)

    if not os.path.exists(file_path):#checking if the file path exists
        print("file was not found.")
        quit()

    here = pathlib.Path(__file__).parent
    hash_folder = here / "key_hashes"
    key = input("Please input a key:\n")#getting the key


    # save a hashed value of the key in a file to prevent issues when decrypting files
    encoded_key = key.encode()
    hashed_key = hashlib.sha256(encoded_key).hexdigest()
    md5_hashed_key = hashlib.md5(encoded_key).hexdigest()# get a md5 hash for encrypting the file

    filename = path.stem
    
    path_to_hash = hash_folder / f"{filename}.keyhash"

    with open(path_to_hash,"w") as file:
        file.write(hashed_key)

    print("Starting encryption process !")

    encrypt(file_path,bytes(md5_hashed_key, encoding="utf-8"))#actually encrypting the file
    print("encryption process successfull")






def init_decrypt():
    """
    This function provides all the other funcionality required to decrypt the file
    """

    #getting the file path
    file_path = input("Please paste the file path in here (full path to the file itself, NOT the folder in which the file is!\n")
    path = pathlib.Path(file_path)

    if not os.path.exists(file_path):#checking if the file path exists
        print("file was not found.")
        quit()

    here = pathlib.Path(__file__).parent
    hash_folder = here / "key_hashes"
    key = input("Please input a key:\n")#getting the key


    # get the hashed key to compare to saves
    encoded_key = key.encode()
    hashed_key = hashlib.sha256(encoded_key).hexdigest()
    md5_hashed_key = hashlib.md5(encoded_key).hexdigest()# get a md5 hash for encrypting the file

    filename = path.stem
    
    path_to_hash = hash_folder / f"{filename}.keyhash"

    with open(path_to_hash,"r") as file:
        actual_hash = file.readline()

    #checking if the saved hash is correct (does a password check, HOWEVER, since there is not a save for every encrypted file, their might be errors)
    if actual_hash != hashed_key:
        continue_choice = input("key might be incorrect. Do you want to continue (might damage the file and it's contents) ?(Y/N)")
        if continue_choice == "Y":
            pass
        else:
            quit
    else:
        print("key correct, starting decryption process !")


    decrypt(file_path,bytes(md5_hashed_key, encoding="utf-8"))# actually decrypting the file
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



