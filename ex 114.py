import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Off-line!')
else:
    print('On-line')
    print(site.read(), end='')



