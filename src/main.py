# Resolve the problem!!
import re

pattern = re.compile(r'[a-z]+')


def run():
    f = open('encoded.txt', 'r', encoding='utf-8')

    for line in f:
        result = re.findall(pattern, line)
        print('Searching...')
        if result:
            print(f'Palabra uno: {result[0]}')
            name = ''.join(result[1:10])
            lastname = ''.join(result[10:16])
            lastname2 = ''.join(result[16:])
            print(f'Palabra dos: {name} {lastname} {lastname2}')
        else:
            print('No se encontraron Datos')
    f.close()


if __name__ == '__main__':
    run()
