
from requests import get, utils

response = get("http://www.cbr.ru/scripts/XML_daily.asp")
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

list_content = content.split("</Value>")


def currency_rates(valute_name):

    for item in list_content:
        if valute_name in item:
            return float(item.split('<Value>')[-1].replace(',', '.')[:-2])

if __name__ == '__main__':

    print(currency_rates('EUR'))
    print(currency_rates('USD'))