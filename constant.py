KEY_FILE = 'key.json'
FILE_NAME = 'Lista de Deseos'
SHEET_NUMBER = 1

STORES = {
    'https://www.falabella.com.co': {
        'tag': ['[data-internet-price]', '[data-normal-price]'],
    },
    'https://www.homecenter.com.co': {
        'tag': ['.product-price .primary'],
    },
    'https://www.exito.com': {
        'tag': [".exito-vtex-components-4-x-valuePLPAllied",
                ".exito-vtex-components-4-x-PricePDP",
                ".exito-vtex-components-4-x-list-price"],
    },
    'https://es.aliexpress.com': {
        'tag': [".product-price-current"]
    },
    'https://www.amazon.com': {
        'tag': [".a-price-whole"]
    }
}
