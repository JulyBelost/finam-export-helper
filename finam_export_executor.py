import finam_export

#  Markets:
#   MosBirzha = 1
#   Bonds = 2
#   Indexes = 6
#   Currencies = 45

#  'emitents' = [(ticker : market)]
portfolios = [
    {'emitents' : [('LKOH', '1'), ('SIBN', '1')]},
    {'emitents' : [('AFLT', '1'), ('BANE', '1')]}
]

for p in portfolios:
    print(p['emitents'])
    finam_export.gather_finam_data(period = finam_export.Period.min,
                                    from_str = '10.01.2012',
                                    to_str = '10.03.2013',
                                    **p)
