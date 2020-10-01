import urllib
import  urllib.request
import webbrowser

try:
    url = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Não está acessivel')
else:
    print('OK')

#webbrowser.open('http://www.pudim.com.br')
