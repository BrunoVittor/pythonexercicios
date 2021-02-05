# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen(input('Digite o site: '))
except urllib.error.URLError:
    print('Deu erro')
else:
    print('Tudo ok')