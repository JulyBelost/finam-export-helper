import urllib, time
import string
import emitent_names
from enum import Enum
from datetime import datetime as dt, timedelta as td


# Here you can choose time period
class Period(Enum):
    tick, min, min5, min10, min15, min30, hour, day, week, month = range(1, 11)

def get_fin_data(market, code, ticker, from_date, to_date, period,
    dtf=3, tmf=2, msor=1, sep=1, sep2=1, datf=1, at=1, fsp=1):

    from_str = from_date.strftime("%d.%m.%Y")
    to_str = to_date.strftime("%d.%m.%Y")

    params  = [ ('market', market),                 #market code
                ('em', code),                       #instrument code
                ('code', ticker),                   #instrument ticker
                ('apply', 0),                       #?
                ('df', from_date.day),              #period start, day
                ('mf', from_date.month-1),          #period start, month
                ('yf', from_date.year),             #period start, year
                ('from', from_str),                 #period start
                ('dt', to_date.day),                #period end, day
                ('mt', to_date.month-1),            #period end, month
                ('yt', to_date.year),               #period end, year
                ('to', to_str),                     #period end
                ('p', period.value),                #period type
                ('f', 'data'),                      #file name
                ('e', '.txt'),                      #file type
                ('cn', ticker),                     #contract name
                ('dtf',  dtf),                      #date format
                ('tmf',  tmf),                      #time format
                ('MSOR', msor),                     #candle time(0-open,1-close)
                ('mstime', 'on'),                   #moscow time (optional)
                ('mstimever', 1),                   #timezone correction
                ('sep',  sep),                      #elements separator
                ('sep2', sep2),                     #digits separator
                ('datf', datf),                     #column selection
                ('at',   at),                       #headers presence (optional)
                ('fsp',  fsp),                      #fill periods w/o trades
    ]

    url = ('http://export.finam.ru/{}.txt?'.format(ticker)
        + urllib.urlencode(params))
    response = urllib.urlopen(url)
    content = response.read()
    return string.split(content, '\n')


def gather_finam_data(emitents, from_str, to_str, period = Period.day):
    """Creates file with aggregated data from finam.ru for given parameters.

    Is able to bypass finam data size restriction by splitting query into
    several requests.

    Args:
        emitents : list of tuples (ticker : market)
        from_str : start date string in "dd.mm.yyyy" format
        to_str   : end date string in "dd.mm.yyyy" format
        period   : granularity of time series represented as Period Enum
    """
    result = []

    from_date = dt.strptime(from_str, "%d.%m.%Y").date()
    to_date = dt.strptime(to_str, "%d.%m.%Y").date()

    for i in range(len(emitents)):
        ticker = emitents[i][0]
        market = emitents[i][1]
        code = emitent_names.define_emitent_code(ticker, market)
        print(ticker, market, code)

        from_var = from_date
        to_var = to_date

        j = 0
        while(to_var >= from_var):
            print(from_var, min(from_var+td(days=364), to_var))
            data = get_fin_data(market, code, ticker, from_var,
                                min(from_var+td(days=364), to_var), period)
            from_var += td(days=365)
            result += data[(0 if (i or j) == 0 else 1):-1]
            j += 1
            time.sleep(1)

    em_str = '_'.join([em[0] for em in emitents])
    filename = 'stocks_{}_{}_{}'.format(em_str,
                                        from_str,
                                        to_str).replace('.', '')
    with open('./' + filename + '.txt', 'w') as f:
        for item in result:
            f.write("{}\n".format(item))
