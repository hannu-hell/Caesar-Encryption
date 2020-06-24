# CAESAR Encription and Decryption

A very simple and basic use of the Caesar ciphering method to encrpt and decrypt phrases and files.
How Caesar Encrpytion works is by providing a key known by both sides for encrption and decryption puroses.  The key can be chosen by any number between **1 - 25** (including 1 and 25).  


## How it works:

Create a Caesar object and use the methods of the Caesar class to encrypt or decrypt.  By adding an amount (determined by the key) of charcters ahead of the character.  To decrypt is by doing away with the characters.


## Methods available:

* encrypt(string) : Encrypts the string passed on to the method.

* decrypt(string) : Decrypts the string passed on to the method.

* encrypt_file(read_file, write_file) : Encrypts a file and saves the encrypted file in the working directory.  The first argument is the file that needs to be encrypted and the second argument is the name of the new file that will be created with the encryption.

* decrypt_file(read_file, write_file) : Decrypts a file and saves the decrypted file in the working directory.  The first argument is the file that needs to be decrypted and the second argument is the name of the new file that will be created with the decryption.

## Usage:

Example : 
----
c = Caesar(3)
print(c.encrypt("hello world"))   # returns 'khoor zruog'
print(c.decrypt("khoor zruog"))   # returns 'hello world'
----


#### LIMITATIONS :

Only encrypts alphabetic characters and numbers.  Special characters are displayed as is.