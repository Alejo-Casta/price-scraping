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

    return df


def open_browser():
    df = get_links_df()
    with sync_playwright() as p:
        browser = p.firefox.launch()
        for data in df['ID']:
            link = df['Link'][data - 1]
            for store in constant.STORES:
                if store['url'] in link:
                    print(link)
                    page = browser.new_page()
                    page.goto(link)
                    try:
                        stock = False if page.wait_for_selector(store['price'],
                                                                timeout=1000) is None else True
                    except:
                        stock = False
                    if stock:
                        content = store['function'](page, store['price'])
                        print(content)
                    page.close()
        browser.close()


open_browser()
