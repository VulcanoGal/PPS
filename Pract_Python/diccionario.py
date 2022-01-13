import json
import re
import os
import pathlib
import hashlib
import json
import yaml
import urllib.request


def prog1(c):
    if c is not None:
        res = re.findall('[0-9]+', c)
        print(res)


def prog2(c):
    if c is not None:
        res = re.split('[0-9]+', c)
        print(res)


def prog3(c):
    if c is not None:
        res = re.sub('[0-9]+', ' ', c)
        print(res)


def prog4(b, c):
    if c is not None and b is not None:
        res = re.search(b, c)
        print(res)


def prog5(c):
    if c is not None:
        res = re.match('986 ', c)
        res2 = re.match('886 ', c)
        if res is None and res2 is None:
            print("Non ten o prefijo de Pontevedra")
        elif res is None:
            print(res2)
        else:
            print(res)


def prog6(c):
    if c is not None:
        iban = c[0:4]
        conta = c[5:15]
        res = re.match('ES', iban)
        if res is None:
            print("A conta non é Española, ou está mal escrita")
        else:
            print(iban)
            print(conta)


def isfloat(num):
    try:
        float(num)
        print("1")
    except ValueError:
        print("F")


def isint(num):
    try:
        int(num)
        print("2")
    except ValueError:
        print("F")


def prog8(c):
    if c is not None:
        ext = pathlib.PurePath(c).suffix
        print(ext)
        ext2 = os.path.split(c)
        print(ext2[0])
        # O '0' e o '1' son as posiciones dos 2 resultados que dá
        print(ext2[1])


def prog9(c):
    if c is not None:
        ext3 = os.path.splitext(c)
        print(ext3[0])
        print(ext3[1])


def prog10():
        lower = int(input("Introduzca un número por pantalla"))
        upper = int(input("Introduzca un número por pantalla"))
        for num in range(lower, upper + 1):
            if num > 1:
                for i in range(2, num):
                    resto = num % i
                    if resto == 0:
                        break
                else:
                    print(num)


def prog11(c):
    if c is not None:
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~+|¡'''
        cad=''
        for char in c:
            if char not in punctuations:
                cad = cad + char

        print(cad)


def prog12(c):
    if c is not None:
        i=1
        print("12")
        while i <= c:
            if c % i == 0:
                print(i)

            i += 1


def prog13(c):
    if c is not None:
        vocales = 'aeiou'
        i = 0
        for char in c:
            if char.lower() in vocales:
                i += 1

        print(i)


def prog14():
    freq = ['a', 1, 'a', 4, 3, 2, 'a'].count('a')
    print(freq)


def prog15(c):
    h = hashlib.sha1()
    with open(c,'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    
    return h.hexdigest()


def prog16(archivo):
    if os.path.exists(archivo):
        file = open(archivo, "r")
        json.load(file)
        file.close()
        print("Este é un archivo JSON")
    else:
        print("Non existe, ou non se puido encontrar o archivo: "+archivo)


def prog17(archivo):
    if os.path.exists(archivo):
        file = open(archivo, "r")
        yaml.safe_load(file.read())
        file.close()
        print("Este é un archivo YAML")
    else:
        print("Non existe, ou non se puido encontrar o archivo: "+archivo)


def prog18(archivo):
    if os.path.exists(archivo):
        ar_or = open(archivo, "r")
        ar_dst = json.load(ar_or)
        ar_or.close()
    else:
        print("ERROR: O archivo  " + archivo + " non existe ou non está no directorio")
        exit(1)
    salida = yaml.dump(ar_dst)
    archivo2 = "proba2.yaml"
    target_file = open(archivo2, "w")
    target_file.write(salida)
    target_file.close()



def prog19(c):
    if c is not None:
        nato_alphabet = {
            'a': 'alpha',
            'b': 'bravo',
            'c': 'charlie',
            'd': 'delta',
            'e': 'echo',
            'f': 'foxtrot',
            'g': 'golf',
            'h': 'hotel',
            'i': 'india',
            'j': 'juliet',
            'k': 'kilo',
            'l': 'lima',
            'm': 'mike',
            'n': 'november',
            'o': 'oscar',
            'p': 'papa',
            'q': 'quebec',
            'r': 'romeo',
            's': 'sierra',
            't': 'tango',
            'u': 'uniform',
            'v': 'victor',
            'w': 'whiskey',
            'x': 'x-ray',
            'y': 'yankee',
            'z': 'zulu'
        }
        for letter in c:
            if letter.lower() not in nato_alphabet:
                print(letter)
            else:
                print(nato_alphabet[letter])
def prog20():
    currency = 'usd'
    basecurrency = 'cad'
    currencyurl = "http://freecurrencyrates.com/api/action.php?do=cvals&iso=" + currency + "&f=" + basecurrency + "&v=1&s=cbr"
    f = urllib.request.urlopen(currencyurl)
    obj = json.loads(f.read())
    result = "1 " + currency.upper() + " is "
    result+="{:,.2f}".format(1/obj[currency.upper()]) + " " + basecurrency.upper()
    print(result);