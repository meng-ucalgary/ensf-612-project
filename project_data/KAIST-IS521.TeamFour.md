TeamFour - Notary Program
=========================
## Install & Usage    
    
### To install python dependencies, follow:
    
```bash
(sudo) ./install.sh
```

### To build flag-updater :
   
```bash
(sudo) make
```

### Usage
    
    Execution Order : Server -> Launcher -> Client

    Server :  (sudo) python notary.py [Key Directory]

    Client :  python client.py [file] [Github ID]

    Launcher : ./launcher [Launcher's IP Address] [Start Server IP Range] [End Server IP Range]

    Flag-Updater : (sudo) ./flagUpdater/flag_updater    

## Protocol

### Notary Program

A. Before start getting a file, Notary Program authenticate the user using PGP keys.

    1. N(Notary) asks client's github ID
    
    2. C(Client) sends github ID.
    
    3. N searches the client's public key in the key repository. If no public key is searched, close the session.
    
    4. N generates a large random Number, sign it with N's private key and encrypts it with client's public key.
    
    5. N sends the encrypted message and C decrypts the message and verify the message.
    
    6. C decrypts it with her/his private key to get the original random number.
    
    7. C encrypts the random number with the server's public key and send the encrypted message back to the server.
    
    8. N verifies the encrypted message.        

B. If C succeeds to authenticate, Notary program gets a signed file from client.

    1. C signs a file with her/his private key and send to the N
        
    2. N verifies sign(also extracts a plain file) and signs it with N's private Key
    
    3. N encodes signed file with base64 and sends it as the json-based bytes to C       
    

### Launcher Program

A. Launcher program gets bytes of json format

    1. L(Launcher) gets json-based bytes from C.

    2. L checks the json-based bytes are right format.
    
    3. If the json-based bytes are right format, L gets name and contents in the json-based bytes.

    4. L makes a base64 file with contents in json-based bytes.

    5. L decrypts the base64 file and gets the gpg file.

    6. L verifies the gpg file with L's public key.

    7. If it is verfied, L executes the file.

    8. If executing file calls 'execve', L terminates it.

### Flag Updater

 A. Flag Updater receives JSON file and verifies their signature and content

    1. The program is daemonized to be runed in background

    2. It listen connection on port 42 and waits that the client send a file

    3. The file is decrypted with the team private key 

    4. The base64 signature is extract from this file and put into a flag file

    5. The file is 64-decoded and put in a gpg file

    6. The informations of the gpg file are checked on order to see if the signature is good

## Misc

1. Notary program is written in Python 2.X

2. Flag updater program is written in C and uses a Python script to decode the  base 64 signature

3. Notary uses JSON format below:
```bash
   {   
   "name": "FROM_[CLIENT-IP]_[YEAR]_[MONTH]_[HOUR]_[MIN]_[Microsecond]",
   "body": "[base64 encoded program executable]"
   }
```
