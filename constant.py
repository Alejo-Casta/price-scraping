KEY_FILE = 'key.json'
FILE_NAME = 'Lista de Deseos'
SHEET_NUMBER = 1


def store_falabella(page, element):
    content = page.get_attribute(element, 'data-internet-price')
    print(content)
    return content


STORES = [
    {
        'url': 'https://www.falabella.com.co',
        'price': '[data-internet-price]',
        'function': store_falabella
    },
    {
        'url': 'https://www.homecenter.com.co',
        'price': '.product-price',
        'out_stock': '.product-price'
    },
    {
        'url': 'https://www.exito.com',
        'price': '.exito-vtex-components-4-x-selling-price',
        'out_stock': '.exito-vtex-components-4-x-selling-price'
    }
]
