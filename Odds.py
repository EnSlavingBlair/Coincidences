#!/usr/bin/env python

from numpy import linspace, ones, insert
import matplotlib.pyplot as plt

#  Using equation 30 from Ashton et al 2018 paper for different values of delta-t

R_fermi_perday = 0.124  # fermi GRB daily detection rate, taken from Ashton et al 2018
R_fermi_persec = R_fermi_perday / 24 / 60 / 60

R_chime_perday = 300  # from Ravi 2019 nature astronomy 3, 928-931
R_chime_persec = R_chime_perday / 24 / 60 / 60

R = R_chime_persec

I_Omega = 32.4  # value taken from Ashton et al paper, for GW170817 and GRB 170817A coincidence

min_time = 0.1
max_time_day = 0.2  # 3  # 1/24  # 262
max_time_hr = max_time_day * 24
max_time_sec = max_time_hr * 60 * 60  # number of seconds in a day
num_step = 100

Delta_t_sec = linspace(min_time, max_time_sec, num=num_step, endpoint=True)
Delta_t_hr = linspace(min_time, max_time_hr, num=num_step, endpoint=True)
Delta_t_day = linspace(min_time, max_time_day, num=num_step, endpoint=True)

odds = I_Omega / (Delta_t_sec * R)

line_100 = ones(num_step)*10**2
line_1 = ones(num_step)

delay_170817_sec = 1.7
delay_170817_hr = delay_170817_sec / (60.0 * 60.0)
delay_170817_day = delay_170817_hr / 24.0
odds_170817 = I_Omega / (delay_170817_sec * R)
#  TODO: Work out why 170817 event does not have the same odds value stated in the paper (~>10^6, eq 30, p6)

odds[0] = odds_170817
Delta_t_day[0] = delay_170817_day

plt.plot(Delta_t_day, odds, label = r"$\mathcal{O}_{C/SS}(D_{GW}, D_{EM}) = \frac{1}{R_{Fermi}} \frac{1}{[\Delta t]} "
                                    r"\mathcal{I}_\Omega$")
plt.plot(Delta_t_day, line_100, label = "Odds of 100")
plt.plot(Delta_t_day, line_1, label = "Odds of 1")
plt.plot(delay_170817_day, odds_170817, 'gx', label = "17/08/17 events")
plt.yscale("log")
plt.ylabel(r"$\mathcal{O}_{C/SS}(D_{GW}, D_{EM})$")
plt.xlabel(r"$\Delta t$"+" (days)")
plt.title("Ashton et al 2018, equation #30")
plt.legend(loc=1)
plt.show()
#plt.savefig("odds_over_time", format="png")
