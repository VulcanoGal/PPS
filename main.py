import requests
import backup


# Función para desmenuzar o contido de flow.txt
# Dentro da función, simplemente separamos os 4 campos en 4 distintas variables para o seu posterior uso dentro do script
def procesar_data(d):
    resultado = None
    if d is not None:
        datos = d.split('|')
        operador = datos[0]
        comando1 = datos[1]
        comando2 = datos[2]
        comando3 = datos[3]
        resultado = operador, comando1, comando2, comando3
    return resultado


if __name__ == '__main__':
    # Sacamos o flow.txt e gardamolo na variable res
    res = requests.get('https://raw.githubusercontent.com/VulcanoGal/PPS/main/flow.txt')
    print(res.text)
    # Leemos el archivo flow.txt, e procesamos o contido ca función creada ao principio do script
    datos = procesar_data(res.text.rstrip('\n'))
    print(datos)

    # Comprobación para saber se facemos backup ou non
    isBackup = datos[1].split(':')[1]
    isAuth = datos[3].split(':')[1]
    # Comprobamos se temos autorización
    if int(isAuth) == 1:
        # Comprobamos si podemos facer backup
        if int(isBackup) == 1:
            backup.backuptoZip('data')
        else:
            print('Non tes activada a función de facer Backup')
    else:
        print('Non tes a autorización necesaria para poder facer o backup')
