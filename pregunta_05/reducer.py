#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

  for line in sys.stdin:

    lista= line.strip().replace('-', ' ').split(' ')

    sys.stdout.write("{}\t1\n".format(lista[4]))
