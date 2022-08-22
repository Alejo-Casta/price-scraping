import re

import pygsheets
from playwright.sync_api import sync_playwright

import constant


def get_links_df():
    # authorization
    client = pygsheets.authorize(service_file=constant.KEY_FILE)

    # open the google spreadsheet
    spreadsheets = client.open(constant.FILE_NAME)

    # select sheet
    sheet = spreadsheets[constant.SHEET_NUMBER]

    # create the dataframe
    df = sheet.get_as_df()
    df['Price'] = 0
    shops = []
    for i in df.index:
        final = df['Link'][i].find('/', 9)
        shops.append(df['Link'][i][0:final])
    df['Shop'] = shops
    return df


def open_browser():
    df = get_links_df()
    with sync_playwright() as p:
        browser = p.firefox.launch()
        context = browser.new_context(storage_state='data.json')
        for i in df.index:
            link = df['Link'][i]
            if df['Shop'][i] in constant.STORES:
                store = constant.STORES[df['Shop'][i]]
                print(link)
                if df['Shop'][i] == 'https://www.amazon.com':
                    page = context.new_page()
                else:
                    page = browser.new_page()
                page.goto(link)
                if df['Shop'][i] == 'https://www.exito.com':
                    page.wait_for_timeout(5000)
                for selector in store['tag']:
                    # page.pause()
                    price_html = page.query_selector(selector)
                    if price_html:
                        price = store['get_price'](re, price_html.text_content())
                        df.loc[i:i, 'Price'] = price
                        print(price)
                        break
        print(df)
        browser.close()


open_browser()
