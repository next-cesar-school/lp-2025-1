import io

try:
    arq = open('exemploq.txt')
    arq.write('teste')
except (FileNotFoundError, io.UnsupportedOperation):
    print('Achei esse arquivo não, visse?')
finally:
    try:
        arq.close()
    except NameError:
        print('O arquivo não foi aberto')
