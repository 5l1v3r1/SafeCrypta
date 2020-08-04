# SafeCrypta
Simple File Encryption in Python using custom seed/key generation


## How Does SafeCrypta Work?
- SafeCrypta uses [pyAesCrypt](https://github.com/marcobellaccini/pyAesCrypt/) to implement AES encryption. What makes SafeCrypta different is the unique key and seed generation which uses pseudo-randomness to generate random digits and random characters from a string of characters. It reseeds the pseudo-random generator with the user's mouse location which is why it is required that you move your mouse randomly around the screen to ensure the key generated is as close to true randomness as possible. 
- SafeCrypta generates seeds by randomly choosing words from a large list of words. The words are chosen with a pseudo-random generator to ensure the words are as close to true randomness as possible. The key/seed is then hashed with SHA512 then removed from memory as fast as possible to remove all traces of the real key/seed.

## Installation
- pyautogui  | This is used to determine the users pointer location
- pyAesCrypt | This is used to implement the AES encryption

`pip install -r requirements.txt`
