import finam_export, emitent_names
import random

#  Markets:
#   MosBirzha = 1
#   Bonds = 2
#   Indexes = 6
#   Currencies = 45
#   US(BATS) = 25, 517
#   bad markets = 91, 519
#
#  'emitents' = [(ticker : market)]

experiment_number = 0

market = '1'
sample_number = 2
portfolio_size = 3
data_folder = ('/Users/julybelost/Dropbox/diploma/portfolio-fixed-share/input/' +
    'finam_raw/no{}/portfolio_size{}'.format(experiment_number, portfolio_size))

emitent_list = emitent_names.get_market_emitents(market)[1]

# set of portfolios to iterate through looks like:
# portfolios = [
#     {'emitents' : [('LKOH', '1'), ('SIBN', '1')]},
#     {'emitents' : [('AFLT', '1'), ('BANE', '1')]}
# ]
portfolios = []
for i in range(sample_number):
    random_emitent_sample = random.sample(emitent_list, portfolio_size)
    random_emitents = [(ticker, market) for ticker in random_emitent_sample]
    random_portfolio = {'emitents' : random_emitents}
    portfolios.append(random_portfolio)

for p in portfolios:
    print(p['emitents'])
    finam_export.gather_finam_data(period = finam_export.Period.min,
                                    from_str = '10.01.2012',
                                    to_str = '10.03.2013',
                                    path = data_folder,
                                    **p)
