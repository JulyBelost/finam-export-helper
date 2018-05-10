import urllib, time
import string
import emitent_names
from enum import Enum
from datetime import datetime as dt


# Here you can choose time period
class Period(Enum):
    tick, min, min5, min10, min15, min30, hour, day, week, month = range(1, 11)

def get_fin_data(market, code, ticker, from_str, to_str, period,
    dtf=3, tmf=2, msor=1, sep=1, sep2=1, datf=1, at=1, fsp=1):

    from_date = dt.strptime(from_str, "%d.%m.%Y").date()
    to_date = dt.strptime(to_str, "%d.%m.%Y").date()

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

#  Markets:
#   MosBirzha = 1
#   Bonds = 2
#   Indexes = 6
#   Currencies = 45
#  (ticker : market)
emitents = [('SBER', '1'), ('AFLT', '1'), ('MSNG', '1'), ('AGRO', '1'),
    ('GTLC', '1'), ('POLY', '1'), ('RUAL', '1'), ('YNDX', '1'), ('QIWI', '1')]
from_str = '01.04.2017'
to_str = '01.04.2018'
period = Period.day
result = []

for i in range(len(emitents)):
    ticker = emitents[i][0]
    market = emitents[i][1]
    code = emitent_names.define_emitent_code(ticker, market)

    data = get_fin_data(market, code, ticker, from_str, to_str, period)

    result += data[(0 if i == 0 else 1):-1]
    time.sleep(1)

# for line in result:
#      print line

with open('./finam_output.txt', 'w') as f:
    for item in result:
        f.write("{}\n".format(item))
