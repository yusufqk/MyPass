## MyPass
This is a command-line tool that serves as a password manager.

## Requirements
Python 3.7 <br />
Linux Distro

## Installation
**Use the following commands:**  
```apt install xsel``` <br />
```pipenv install``` <br />
```pipenv shell``` <br />
```python setup.py```

*Note: The packages are automatically installed using the pipenv tool. For more info see [pipenv](https://docs.pipenv.org/en/latest/basics/)

**Usage:**
```python mypass.py```

## Features
**Four Modules**:
Four modules are available: Adder, Deleter, Modifier, Viewer. The adder allows the user to add accounts, deleter removes them, and modifier changes them to the user's needs. Viewer pastes the password for an account to your clipboard to allow for sign in. The clipboard is cleared after 20 seconds

**AutoTab Completion**: 
Switching between modules is made easy by autotab 

## How it Works
The setup script generates RSA keys (4096 bit length) and uses the supplied master password as the AES key. The AES key is used to encrypt the private key and the public key encrypts the passwords text document. When the user signs in with their master password, the private key is decrypted using the AES key (master password) and is subsequently used to decrypt the password document. 

## Future Improvements
One shortcoming is the Master Password must be 16 characters long, so that the user must enter and memorize a 16 character string. This clearly sucks from the user's perspectve. Also, at this moment there is no automatic way to reinstate the password and associated keys. Future commits will attempt to address these issues. 

## Contributions
The ability to switch easily between the four modules was learnt from @byt3bl33d3r's SILENTTRINITY application. 




