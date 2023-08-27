from fredapi import Fred
from matplotlib import pyplot as plt

fred = Fred(api_key='6e724faa9cebe8b2662e4e0f5f832fc3')

sp500 = fred.get_series('SP500')

rate_10Y = fred.get_series('DGS10')
rate_2Y = fred.get_series('DGS2')
rate_3M = fred.get_series('DGS3MO')

plt.plot(sp500)
plt.plot(rate_10Y)
plt.plot(rate_2Y)
plt.plot(rate_3M)