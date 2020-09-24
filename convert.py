from forex_python.converter import CurrencyRates, CurrencyCodes

# available_currencies = ["EUR","IDR","BGN","ILS","GBP","DKK","JPY","CAD",
# "HUF","RON","MYR","SEK","SGD","HKD","AUD","CHF","KRW", "CNY","TRY","HRK","NZD","THB","USD","NOK","RUB","INR","MXN","CZK","BRL","PLN","PHP","ZAR"]


def check_currency_code(currency_code):
    return CurrencyCodes().get_currency_name(currency_code) is not None

def currency_rate(convert_from, convert_to, amount):
    """Convert Currency rate"""
    res = round(CurrencyRates().convert(convert_from, convert_to, amount), 2)
    return res

def currency_code(convert_to):
    """ Get curency code """

    res = CurrencyCodes().get_symbol(convert_to)
    return res