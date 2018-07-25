import finam_export, emitent_names
import random
from distutils.dir_util import mkpath

#  Markets:
#   MosBirzha = 1
#   MosBirzha top = 200
#   ? = 8
#   Bonds = 2
#   Indexes = 6
#   Currencies = 45
#   US(BATS) = 25, 517
#   bad markets = 91, 519
#
#  'emitents' = [(ticker : market)]

experiment_number = '0'

market = '200'
sample_number = 2
portfolio_size = 2
data_folder = ('/Users/julybelost/Documents/portfolio-fixed-share/' +
               'exp{}_market{}/portf_size{}/'.format(experiment_number,
                                                     market,
                                                     portfolio_size))
download_path = data_folder + 'input/finam_raw/'

mkpath(download_path)
mkpath(data_folder + 'results/plot_data/')

print('result files will be in ' + download_path)


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
                                   from_str = '08.01.12',
                                   to_str = '08.07.18',
                                   path = download_path,
                                   **p)
