import urllib
import string

tm_to_code = {}
markts = {}
emitents = {}

def load_finam_vars():
    url = 'http://www.finam.ru/cache/icharts/icharts.js'
    url2 = 'http://www.finam.ru/scripts/export.js'

    response = urllib.urlopen(url).read()
    finam_var_list = string.split(response, '\n')

    js_vars = {}

    # create js_vars with 'codes', 'tickers', 'markets' lists
    for key, v in {'codes': 0, 'tickers': 2, 'markets': 3}.iteritems():
        s = finam_var_list[v]
        js_vars[key] = (s[s.find('[') + 1 : s.find(']')].split(','))

    global tm_to_code, markts, emitents
    for c,t,m in zip(js_vars['codes'],js_vars['tickers'],js_vars['markets']):
        tm_to_code[(t,m)] = c
        markts.setdefault(t, []).append(m)
        emitents.setdefault(m, []).append(t.strip('\''))


def define_emitent_code(ticker, market):
    global tm_to_code
    if not tm_to_code:
        load_finam_vars()

    name = "'{}'".format(ticker)

    return tm_to_code[(name, market)]


def get_emitent_markets(ticker):
    global markts
    if not markts:
        load_finam_vars()

    name = "'{}'".format(ticker)

    return (ticker, sorted(markts[name]))


def get_market_emitents(market):
    global emitents
    if not emitents:
        load_finam_vars()

    return (market, sorted(emitents[market]))
