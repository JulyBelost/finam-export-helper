import urllib
import string

def get_fin_data(ticker = 'AFLT', em = 29):
    filename = ticker + '_180503_180503'
    params  = [ ('market', 1),
                ('em', em),
                ('code', ticker),
                ('apply', 0),
                ('df', 3),
                ('mf', 4),
                ('yf', 2018),
                ('from', '03.05.2018'),
                ('dt', 3),
                ('mt', 4),
                ('yt', 2018),
                ('to', '03.05.2018'),
                ('p', 7),
                ('f', filename),
                ('e', '.txt'),
                ('cn', ticker),
                ('dtf',  1),
                ('tmf',  1),
                ('MSOR', 1),
                ('mstime', 'on'),
                ('mstimever', 1),
                ('sep',  1),
                ('sep2', 1),
                ('datf', 1),
                ('at',   1)
    ]

    url = ('http://export.finam.ru/{}.txt?'.format(filename)
        + urllib.urlencode(params))
    response = urllib.urlopen(url)
    content = response.read()
    print url
    return string.split(content, '\n')

data = get_fin_data('SBER', 3)
for line in data:
    print line
