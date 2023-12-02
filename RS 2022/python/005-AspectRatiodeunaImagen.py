'''
* Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/
 *   mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
'''
import requests
from PIL import Image
from io import BytesIO

url = 'https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png'
def getAspectRatio(url):
    try:
        # Obtenemos la imagen
        r = requests.get(url)
        r.raise_for_status()
        # La convertimos en un objeto Image
        image = Image.open(BytesIO(r.content))
        # Mostramos la imagen para ver lo que es
        image.show()
        # Obtenemos el aspect ratio
        width, height = image.size
        aspect_ratio = width/height

        return aspect_ratio, width, height
    # Capturamos el error en caso de que la url no sea correcta
    except Exception as err:
        raise f'Error: {err}'
    

aspect_ratio, width, height = getAspectRatio(url)

# Mostramos el resultado
# Si el aspect ratio es un float, lo mostramos con dos decimales
if isinstance(aspect_ratio, float):
    print(f'El aspect ratio de la imagen es: {aspect_ratio:.2f}')

else:
    print(aspect_ratio)

# Mostramos el tamaño de la imagen
print(f'La imagen tiene un tamaño de {width}x{height} pixeles')


