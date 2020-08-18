#!/usr/bin/env python

from numpy import linspace, ones
import matplotlib.pyplot as plt

#  Using equation 30 from Ashton et al 2018 paper for different values of delta-t

R_fermi_perday = 0.124  # fermi GRB daily detection rate, taken from Ashton et al 2018
R_fermi_persec = R_fermi_perday / 24 / 60 / 60

I_Omega = 32.4  # value taken from Ashton et al paper, for GW170817 and GRB 170817A coincidence

min_time = 0
max_time_day = 1/24  # 262
max_time_hr = max_time_day * 24
max_time_sec = max_time_hr * 60 * 60  # number of seconds in a day
num_step = 100

Delta_t_sec = linspace(min_time, max_time_sec, num=num_step, endpoint=True)
Delta_t_hr = linspace(min_time, max_time_hr, num=num_step, endpoint=True)
Delta_t_day = linspace(min_time, max_time_day, num=num_step, endpoint=True)

odds = I_Omega / (Delta_t_sec * R_fermi_persec)

one_line = ones(num_step)

delay_170817_sec = 1.7
delay_170817_hr = delay_170817_sec / (60.0 * 60.0)
delay_170817_day = delay_170817_hr / 24.0
odds_170817 = I_Omega / (delay_170817_sec * R_fermi_persec)

plt.plot(Delta_t_day, odds)
plt.plot(Delta_t_day, one_line)
plt.plot(delay_170817_day, odds_170817, 'gx')
plt.yscale("log")
plt.ylabel("Significance")
plt.xlabel("Time (days)")
plt.title("Odds Equation (#30 from Ashton et al 2018)")
plt.show()
