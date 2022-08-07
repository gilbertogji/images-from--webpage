from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
x1x=0
x2x=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#obtener la pagina y parse con BeautifulSoup
url = input('escriba la pagina: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


print('\ntodas las imagenes en la pagina:\n(se despliegan primero todas las imagenes de la pagina y posteriormente las imagenes que si nos interesan)\n(se basa en encontrar imagenes con la palabra denuncia en alguna parte de su nombre)\n')
#print('(imagenes con attributo data-lazyload, puede haber mas imagenes, pero serian descartables')
x=soup.find_all('img')
for y in x:
    x1x=x1x+1
    if 'data-lazyload' in y.attrs:
        print('url: ', y.attrs['data-lazyload'])

#solo dar lo surl de las imagens que tiene denuncia en su nombre
print('\nlas imagenes que nos interesan: ')
for y in x:
    if 'data-lazyload' in y.attrs:
        if re.search('//\S+denuncia\S+', y.attrs['data-lazyload']) is not None:
            print('url(imagenesque nos interesan): ', y.attrs['data-lazyload'])
            x2x=x2x+1

print('imagenes en total: ', x1x)
print('imagenes con denuncia en el nombre: ', x2x)
