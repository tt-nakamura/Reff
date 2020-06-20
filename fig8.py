import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from Reff import Reff

# data from
# https://data.london.gov.uk/dataset/coronavirus--covid-19--cases
data = pd.read_csv('phe_cases_london_england.csv')
data = data[data['area_name'] == 'London']
t = np.array(pd.to_datetime(data['date']), 
             dtype='datetime64[D]').astype(np.float)
c = np.array(data['new_cases'])

d = 20 # omit plotting for first d days

plt.figure(figsize=(6.4, 6))

plt.subplot(2,1,1)
plt.bar(t,c)
plt.xlim(t[[d,-1]])
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
plt.ylabel('number of incidence', fontsize=14)

tau = 7 # length of time window
si_mean = 6.3 # mean of serial interval
si_std = 4.2 # standard deviation of serial interval
conf = 0.95 # confidence level of estimated Reff

R = Reff(c, si_mean, si_std, tau, conf)

plt.subplot(2,1,2)
plt.semilogy(t[d:], R[0,d:], 'r', label='median')
plt.semilogy(t[d:], R[1,d:], 'k--')
plt.semilogy(t[d:], R[2,d:], 'k--', label='95% confidence')
plt.semilogy(t[[d,-1]], [1,1], 'g:')
plt.xlim(t[[d,-1]])
plt.ylabel(r'$R_{\rm eff}$', fontsize=14)
plt.legend(fontsize=14)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))

plt.tight_layout()
plt.savefig('fig8.eps')
plt.show()
