import matplotlib.pyplot as plt
from Reff import si_distr

N = 25
si_mean = 6.3 # mean of serial interval
si_sd = 4.2 # standard deviation of serial interval

w = si_distr(N, si_mean, si_sd)
plt.bar(range(N), w)
plt.xlim([0, N-0.5])
plt.xlabel('$s$ = serial interval  / days', fontsize=14)
plt.ylabel(r'$w_s$ = probability of reproduction', fontsize=14)
plt.text(19, 0.13, r'$E(s) = 6.3$ d', fontsize=14)
plt.text(19, 0.12, r'$\sigma(s) = 4.2$ d', fontsize=14)
plt.tight_layout()
plt.savefig('fig1.eps')
plt.show()
