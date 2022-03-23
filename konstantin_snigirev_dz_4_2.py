from requests import get, utils


# response = get('http://www.cbr.ru/scripts/XML_daily.asp')
#
# encodings = utils.get_encoding_from_headers(response.headers)
# content = response.content.decode(encoding=encodings)
# print(content)

def currency_rates(ticket):

    target_url = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(target_url.headers)
    target_content = target_url.content.decode(encoding=encodings)

    key_words = ['Nominal', 'Name', 'Value']
    target_currency = target_content[target_content.find(str(ticket).upper()):]

    if len(target_currency) > 2:
        target_currency = target_currency[:target_currency.find('</Valute>')]
        currency_info = list(map(lambda x: str(target_currency.split(x)[1])[1:-2], key_words))
        currency_info[0] = int(currency_info[0])
        currency_info[2] = float('.'.join(currency_info[2].split(',')))

        print(f'За {currency_info[0]} {currency_info[1]} дают {currency_info[2]} рублей')
    else:
        print(None)


currency_rates(input('Enter ticket: '))
