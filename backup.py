import os
import zipfile


def backuptoZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    # Un pequeno contador co cal intentaremos que non existan arquivos co mesmo nome, para así
    # non sobreescribir os antigos
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number = number + 1

    # Creamos o arquivo.zip, e dispoñemos a enchelo ca carpeta que nos lle indicamos previamente no script main.py
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # Con este pequeno bucle, imos recorrendo todas as carpetas ata chegar ao destino
    # metendo os arquivos que estén dentro, no arquivo.zip
    for foldername, subfolders, filenames in os.walk(folder):
        backupZip.write(foldername)
        for filename in filenames:
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Fin do backup')
