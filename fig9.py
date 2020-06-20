import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from Reff import Reff

# data from:
# https://www.arcgis.com/home/item.html?id=f10774f1c63e40168479a1feb6c7ca74
data = pd.read_csv('RKI_COVID19.csv')
data = data[data['Bundesland'] == 'Berlin']
date = np.array(pd.to_datetime(data['Refdatum']))

t = np.arange('2020-02-17', '2020-06-01', dtype=np.datetime64)
c = np.count_nonzero(date[:,np.newaxis] == t, axis=0)
t = t.astype(np.float)

plt.figure(figsize=(6.4, 6))

plt.subplot(2,1,1)
plt.bar(t,c)
plt.xlim(t[[0,-1]])
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
plt.ylabel('number of incidence', fontsize=14)

tau = 7 # length of time window
si_mean = 6.3 # mean of serial interval
si_std = 4.2 # standard deviation of serial interval
conf = 0.95 # confidence level of estimated Reff
d = tau # omit plotting for first d days

R = Reff(c, si_mean, si_std, tau, conf)

plt.subplot(2,1,2)
plt.semilogy(t[d:], R[0,d:], 'r', label='median')
plt.semilogy(t[d:], R[1,d:], 'k--')
plt.semilogy(t[d:], R[2,d:], 'k--', label='95% confidence')
plt.semilogy(t[[0,-1]], [1,1], 'g:')
plt.xlim(t[[0,-1]])
plt.ylabel(r'$R_{\rm eff}$', fontsize=14)
plt.legend(fontsize=14)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))

plt.tight_layout()
plt.savefig('fig9.eps')
plt.show()
