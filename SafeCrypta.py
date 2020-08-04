import os
import time
import random
import hashlib
import getpass
import requests
import pyautogui
import pyAesCrypt
from pyautogui import position


chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'

def encryption():
    print('Which key generation technique would you like to use (Use 1, 2 or 3)')
    tech = input(
        '[1] Random Seed/[2] Use existing seed/[3] Random KeyFile>>> ')
    if tech == '1':
        print('[*] Please wait while we get the environment...')
        tech = None
        res = requests.get(
            'http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain')
        words = ''
        for i in range(random.randint(10, 15)):
            words += random.choice(res.content.splitlines()
                                   ).lower().decode("utf-8") + ' '
        print('Printing your seed for 15 seconds, then it will be destroyed')
        print(words)
        seed = words
        words = None
        time.sleep(15)
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print('[*] Cleared Environment')
        seeds = getpass.getpass('Please input the seed>>> ')
        seeds = seeds.replace(" ", "")
        if seeds != seed.replace(" ", ""):
            print('You have incorrectly entered the seed!')
            exit()
        else:
            print('Congrats, the seed you entered was correct')
            seed = None
            seedHash = hashlib.sha3_512(str.encode(seeds)).digest()
            seeds = None
            filename = input('Enter the name of the file>> ')
            pyAesCrypt.encryptFile(
                filename, filename + '.safec', str(seedHash), 64 * 1024)
            print(
                f'[*] Succesfully encrypted {filename} into archive {filename}.safec')
    if tech == '2':
        print('[*] Please wait while we get the environment...')
        tech = None
        seed = getpass.getpass('Please input your seed>>> ')
        seedHash = str(hashlib.sha3_512(str.encode(seed)).digest())
        seed = None
        filename = input('Enter the name of the file>> ')
        pyAesCrypt.encryptFile(filename, filename +
                               '.safec', seedHash, 64 * 1024)
        os.remove(filename)
        print(
            f'[*] Succesfully encrypted {filename} into archive {filename}.safec')
        seedHash = None
    if tech == '3':
        print('[*] Please wait while we get the environment...')
        tech = None
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print('[*] Please move your mouse around your screen')
        # Ensure the user is moving their mouse around the screen
        time.sleep(2)
        random.seed(pyautogui.position()[0] + 7j * pyautogui.position()[1])
        randomKeys = []
        for i in range(random.randint(5, random.randint(10, 30))):
            time.sleep(random.random())
            seed = pyautogui.position()[0] + 9j * pyautogui.position()[1]
            random.seed(seed)
            if random.random() >= random.random():
                integer = str(random.random()).split('.')
                randomKeys.append(''.join(random.choice(chars) for i in range(
                    random.randint(0, 50))) + integer[1] + random.choice(chars) + integer[0])
            else:
                integer = str(random.random()).split('.')[1]
                randomKeys.append(integer + random.choice(chars) * 5 + ''.join(
                    random.choice(chars) for i in range(random.randint(0, 50))))
        random.seed(pyautogui.position()[
                    0] + 6j * int(str(int(str(time.time()).split('.')[1]) / 100).split('.')[0]))
        random.shuffle(randomKeys)
        random.seed(pyautogui.position()[
                    1] + 4j * int(str(int(str(time.time()).split('.')[1]) / 100).split('.')[0]))
        random.shuffle(randomKeys)
        random.seed(pyautogui.position()[0] + 1j * pyautogui.position()[1])
        trueKey = random.choice(randomKeys)
        print('[*] The random key has been generated, exporting to Key.safek')
        with open('Key.safek', 'w') as f:
            f.write(str(trueKey))
            trueKey = str(hashlib.sha3_512(str.encode(trueKey)).digest())
        print('[*] The random key has been exported')
        filename = input('Enter the name of the file>> ')
        pyAesCrypt.encryptFile(filename, filename +
                               '.safec', trueKey, 64 * 1024)
        trueKey = None
        os.remove(filename)
        print(
            f'[*] Succesfully encrypted {filename} into archive {filename}.safec')


def decryption():
    print('Which method would you like to use for decryption (Use 1 or 2)')
    tech = input('[1] Use a seed or passphrase/[2] Use a KeyFile>>> ')
    if tech == '1':
        tech = None
        seeds = getpass.getpass('Please input the seed/passphrase>>> ')
        seeds = seeds.replace(" ", "")
        seeds = str(hashlib.sha3_512(str.encode(seeds)).digest())
        filename = input('Enter the name of the file>> ')
        try:
            pyAesCrypt.decryptFile(filename, filename.split(
                '.')[0] + '.' + filename.split('.')[1], seeds, 64 * 1024)
        except Exception as e:
            print(e)
            exit()
        print('[*] Cleaning environment...')
        seeds = None
        os.remove(filename)
        exportedFile = filename.split(".")[0] + "." + filename.split(".")[1]
        print(
            f'[*] Succesfully decrypted {filename} into raw file {exportedFile}')
    if tech == '2':
        tech = None
        keyFile = input('Enter the name of the KeyFile>> ')
        filename = input('Enter the name of the file>> ')
        with open(keyFile, 'r') as key:
            keys = str(hashlib.sha3_512(
                str.encode(key.read().strip())).digest())
        try:
            pyAesCrypt.decryptFile(filename, filename.split(
                '.')[0] + '.' + filename.split('.')[1], keys, 64 * 1024)
        except Exception as e:
            print(e)
            exit()
        keys = None
        exportedFile = filename.split(".")[0] + "." + filename.split(".")[1]
        os.remove(filename)
        print(
            f'[*] Succesfully decrypted {filename} into raw file {exportedFile}')


def generation():
    tech = input('[1] Generate random seed//[2] Generate random KeyFile>> ')
    if tech == '1':
        print('[*] Please wait while we get the environment...')
        tech = None
        res = requests.get(
            'http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain')
        words = ''
        for i in range(random.randint(10, 15)):
            words += random.choice(res.content.splitlines()
                                   ).lower().decode("utf-8") + ' '
        print('Printing your seed for 15 seconds, then it will be destroyed')
        print(words)
        time.sleep(15)
        words = None
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        exit()

    if tech == '2':
        print('[*] Please wait while we get the environment...')
        tech = None
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print('[*] Please move your mouse around your screen')
        # Ensure the user is moving their mouse around the screen
        time.sleep(2)
        random.seed(pyautogui.position()[0] + 7j * pyautogui.position()[1])
        randomKeys = []
        for i in range(random.randint(5, random.randint(10, 30))):
            time.sleep(random.random())
            seed = pyautogui.position()[0] + 9j * pyautogui.position()[1]
            random.seed(seed)
            if random.random() >= random.random():
                integer = str(random.random()).split('.')
                randomKeys.append(''.join(random.choice(chars) for i in range(
                    random.randint(0, 50))) + integer[1] + random.choice(chars) + integer[0])
            else:
                integer = str(random.random()).split('.')[1]
                randomKeys.append(integer + random.choice(chars) * 5 + ''.join(
                    random.choice(chars) for i in range(random.randint(0, 50))))
        random.seed(pyautogui.position()[
                    0] + 6j * int(str(int(str(time.time()).split('.')[1]) / 100).split('.')[0]))
        random.shuffle(randomKeys)
        random.seed(pyautogui.position()[
                    1] + 4j * int(str(int(str(time.time()).split('.')[1]) / 100).split('.')[0]))
        random.shuffle(randomKeys)
        random.seed(pyautogui.position()[0] + 1j * pyautogui.position()[1])
        trueKey = random.choice(randomKeys)
        exportWhere = input('Filename to export to>> ')
        print(
            f'[*] The random key has been generated, exporting to {exportWhere}')
        with open(exportWhere, 'w') as f:
            f.write(str(trueKey))
            trueKey = str(hashlib.sha3_512(str.encode(trueKey)).digest())
        print('[*] The random key has been exported')


def main():
    print('Welcome to SafeCrypta | v1.0 File Encryption')
    print('''
What would you like to do:
    1.) Encrypt a file
    2.) Decrypt a file
    3.) Generate a random key''')
    userInput = input('Option> ')
    if str(userInput):
        if userInput.lower().startswith('e'):
            print('[*] Switching to encryption environment, please wait')
            encryption()
        elif userInput.lower().startswith('d'):
            print('[*] Switching to decryption environment, please wait')
            decryption()
        elif userInput.lower().startswith('r') or userInput.lower().startswith('g'):
            print('[*] Switching to generating environment, please wait')
            generation()
        elif userInput == '1':
            print('[*] Switching to encryption environment, please wait')
            encryption()
        elif userInput == '2':
            print('[*] Switching to decryption environment, please wait')
            decryption()
        elif userInput == '3':
            print('[*] Switching to generating environment, please wait')
            generation()
        else:
            print('[!] Exitting...')
            exit()

    else:
        print('[!] Exitting...')
        exit()


main()
