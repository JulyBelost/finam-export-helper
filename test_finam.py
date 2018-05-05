import urllib
import string

def get_fin_data():
    response = urllib.urlopen('http://export.finam.ru/AFLT_180503_180503.txt?market=1&em=29&code=AFLT&apply=0&df=3&mf=4&yf=2018&from=03.05.2018&dt=3&mt=4&yt=2018&to=03.05.2018&p=7&f=AFLT_180503_180503&e=.txt&cn=AFLT&dtf=1&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=1&at=1')
    content = response.read()
    return string.split(content, '\n')

data = get_fin_data()
for line in data:
    print line
