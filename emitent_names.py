import urllib
import string

vars = {}
markts = {}

def load_finam_vars():
    url = 'http://www.finam.ru/cache/icharts/icharts.js'
    url2 = 'http://www.finam.ru/scripts/export.js'

    response = urllib.urlopen(url).read()
    finam_var_list = string.split(response, '\n')

    js_vars = {}

    for key, v in {'codes': 0, 'tickers': 2, 'markets': 3}.iteritems():
        s = finam_var_list[v]
        js_vars[key] = (s[s.find('[') + 1 : s.find(']')].split(','))

    global vars, markts
    for c,t,m in zip(js_vars['codes'],js_vars['tickers'],js_vars['markets']):
        vars[(t,m)] = c
        if (t in markts):
            markts[t].append(m)
        else: markts[t] = [m]


def define_emitent_code(ticker, market):
    global vars
    if not vars:
        load_finam_vars()

    name = "'{}'".format(ticker)

    return vars[(name, market)]


def define_emitent_markets(ticker):
    global markts
    if not markts:
        load_finam_vars()

    name = "'{}'".format(ticker)

    return (ticker, sorted(markts[name]))

# TODO
# def all_market_emitents(market):
#     return sorted(emitents[market])
