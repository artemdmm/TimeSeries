import os
from os import path
from matplotlib import pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from pylab import rcParams

rcParams['figure.figsize'] = 11, 9

dirname = os.path.abspath(os.curdir) + r'\data\underwork\5'
tsdf_c = pd.read_csv(path.join(os.sep, dirname, 'calm_p.csv'))
tsdf_c.set_index('Time').sort_index()

passengers = pd.read_csv('data/passengers.csv')
passengers['Month'] = pd.to_datetime(passengers['Month'])
df = passengers.set_index('Month').sort_index()

exchange_rates = pd.read_csv('data/Daily foreign exchange rates AustraliaUS BritishUS CanadianUS DutchUS .csv')
exchange_rates[] = 

decompose = seasonal_decompose(passengers["Passengers"], period=10)
decompose.plot()
plt.show()
