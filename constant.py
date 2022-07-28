KEY_FILE = 'key.json'
FILE_NAME = 'Lista de Deseos'
SHEET_NUMBER = 1


def get_price_standar(re, price):
    pattern = re.compile('[^0-9]')
    return pattern.sub('', price)


def get_price_aliexpress(re, price):
    first = price.find('-')
    if first != -1:
        price = price[first:-2]
    else:
        price = price[0:-2]
    return get_price_standar(re, price)


STORES = {
    # 'https://www.falabella.com.co': {
    #     'tag': ['[data-internet-price]', '[data-normal-price]'],
    #     'get_price': get_price_standar
    # },
    # 'https://www.homecenter.com.co': {
    #     'tag': ['.product-price .primary'],
    #     'get_price': get_price_standar
    # },
    # 'https://www.exito.com': {
    #     'tag': ['.exito-vtex-components-4-x-valuePLPAllied',
    #             '.exito-vtex-components-4-x-PricePDP',
    #             '.exito-vtex-components-4-x-list-price'],
    #     'get_price': get_price_standar
    # },
    # 'https://es.aliexpress.com': {
    #     'tag': ['.product-price-current'],
    #     'get_price': get_price_aliexpress
    # },
    'https://www.amazon.com': {
        'tag': ['.a-price-whole'],
        'get_price': get_price_standar
    }
}
