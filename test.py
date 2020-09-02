from astropy import coordinates as apc
import numpy as np
import itertools
import re
from matplotlib import pyplot as plt

def gaussian(x, mu, sig):
    # returns a Gaussian of mean mu, standard deviation sig, across x-axis x
    # e^(-(x - mu)^2 / (2 * sig^2))
    return [np.exp(-np.power(elem - mu, 2.) / (2 * np.power(sig, 2.))) for elem in x]

# NGC 4993 Metric Distance Gaussian data; mu, sigma, min of x-axis (x1), max of x-axis (x2)
galaxy_mean = 38.909
galaxy_stdev = 4.251
galaxy_min = 31.000
galaxy_max = 44.000

# GW distance Gaussian data; mu, sigma, min of x-axis (x1), max of x-axis (x2)
gw_mean = 40
gw_stdev = 8

gw_eff_file = "GW_efficiency/GW_Eff_funct_2G_2pt5G.txt"

data = []
with open(gw_eff_file, 'r') as f:
    # start at line 4 and stop at 4
    for line in itertools.islice(f, 4, 5):
        col_names = line[:-1]
        col_names = col_names.split(" | ")
    # start at line 5 (0, because last loop ended on 5) and never stop (None), until the end
    for line in itertools.islice(f, 0, None):
        data.append(re.split(' ;|  ;',line[:-1]))

# put data from file into lists
redshift = []
o3_joint_orig = []
o3_gw_only_orig = []
for entry in data:
    redshift.append(float(entry[0]))
    o3_joint_orig.append(float(entry[3]))
    o3_gw_only_orig.append(float(entry[4]))


x_axis = [apc.Distance(z = elem) for elem in redshift]  # turn array of redshift values into Mpc values
z_scalar = [z.value for z in x_axis]

galaxy_gauss = gaussian(z_scalar, galaxy_mean, galaxy_stdev)
gw_gauss = gaussian(z_scalar, gw_mean, gw_stdev)

plt.plot(z_scalar, galaxy_gauss, color = 'cornflowerblue', label = 'NGC 4993 Metric Distance')
plt.plot(z_scalar, gw_gauss, color='purple', label='Gravitational Waves')

plt.plot(z_scalar, o3_joint_orig, color = 'lightgreen', label = 'Efficiency O3 Joint')
plt.plot(z_scalar, o3_gw_only_orig, color = 'mediumseagreen', label = 'Efficiency O3 GW only')

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('Distance Estimates for the 17/08/17 events')
plt.xlabel('Distance (Mpc)')
plt.ylabel('Normalised PDF')
plt.xticks(rotation=90)
left, right = plt.xlim()
plt.xlim(10, 70)
plt.legend()
plt.show()

'''
value = np.linspace(31, 44, 100)
mpc_dist = apc.Distance(value, apu.Mpc)
redshift = [apc.Distance.compute_z(elem) for elem in mpc_dist]

mean_z = apc.Distance.compute_z(apc.Distance(38.909, apu.Mpc))
min_z = apc.Distance.compute_z(apc.Distance(38.909-4.251, apu.Mpc))
max_z = apc.Distance.compute_z(apc.Distance(38.909+4.251, apu.Mpc))

diff = (mean_z - min_z) - (max_z - mean_z)

z_values = [apc.Distance(z = elem) for elem in redshift]  # turn array of redshift values into Mpc values
'''