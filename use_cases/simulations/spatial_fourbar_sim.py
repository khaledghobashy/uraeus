# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:47:07 2019

@author: khaled.ghobashy
"""
import numpy as np
import matplotlib.pyplot as plt

from source.solvers.python_solver import solver

import use_cases.generated_templates.assemblies.spatial_fourbar_assm as assm
from use_cases.generated_templates.configurations import spatial_fourbar_cfg

assm.FB.config = spatial_fourbar_cfg.configuration()
assm.FB.config.load_from_csv(r'C:\Users\khaled.ghobashy\Desktop\Khaled Ghobashy\Mathematical Models\asurt_cdt_symbolic\use_cases\generated_templates\configurations\csv_files\spatial_fourbar_mod.csv')

assm.FB.config.AF_jcs_rev_crank = lambda t: -np.pi*t

assembled = assm.numerical_assembly()
assembled.set_gen_coordinates(assembled.q0)
soln = solver(assembled)

soln.set_time_array(5, 500)
soln.solve_kds('spatial_fourbar_temp.csv', save=True)

time_array = soln.time_array

plt.figure(figsize=(8, 4))
plt.plot(time_array, soln.pos_dataframe['FB.rbs_crank.z'])
plt.legend()
plt.grid()
plt.show()


plt.figure(figsize=(8, 4))
plt.plot(time_array, soln.pos_dataframe['FB.rbs_coupler.z'])
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(time_array, soln.pos_dataframe['FB.rbs_rocker.z'])
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(time_array, soln.vel_dataframe['FB.rbs_rocker.z'])
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(time_array, soln.acc_dataframe['FB.rbs_rocker.z'])
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(time_array, soln.acc_dataframe['FB.rbs_rocker.z'])
plt.plot(time_array, np.gradient(soln.vel_dataframe['FB.rbs_rocker.z'],0.01))
plt.legend()
plt.grid()
plt.show()

d = '''
-184.7272
-114.2975
-45.42616
22.0011
88.11169
153.0439
216.9449
279.9693
342.2771
404.0321
465.4005
526.5492
587.6441
648.8484
710.3205
772.212
834.6651
897.81
961.7615
1026.615
1092.444
1159.291
1227.169
1296.046
1365.847
1436.441
1507.632
1579.154
1650.657
1721.701
1791.744
1860.132
1926.095
1988.737
2047.035
2099.84
2145.882
2183.78
2212.066
2229.203
2233.627
2223.789
2198.202
2155.504
2094.519
2014.32
1914.296
1794.202
1654.214
1494.958
1317.527
1123.477
914.8033
693.8949
463.4712
226.5035
-13.87456
-254.4618
-492.0849
-723.6893
-946.4209
-1157.695
-1355.252
-1537.192
-1702.005
-1848.569
-1976.149
-2084.379
-2173.232
-2242.984
-2294.183
-2327.597
-2344.18
-2345.026
-2331.332
-2304.362
-2265.416
-2215.797
-2156.794
-2089.657
-2015.583
-1935.701
-1851.068
-1762.659
-1671.365
-1577.992
-1483.257
-1387.799
-1292.173
-1196.858
-1102.263
-1008.726
-916.5264
-825.8849
-736.9711
-649.9074
-564.7744
-481.6155
-400.4409
-321.232
-243.9449
-168.5139
-94.85486
-22.86812
47.55899
116.5495
184.2344
250.7508
316.2395
380.8429
444.7037
507.9622
570.7547
633.2112
6.95E+02
7.58E+02
8.20E+02
8.82E+02
9.44E+02
1.01E+03
1.07E+03
1.13E+03
1.20E+03
1.26E+03
1.32E+03
1.38E+03
1.45E+03
1.51E+03
1.57E+03
1.62E+03
1.68E+03
1.73E+03
1.78E+03
1.82E+03
1.86E+03
1.89E+03
1.92E+03
1.93E+03
1.94E+03
1.93E+03
1.91E+03
1.88E+03
1.84E+03
1.78E+03
1.70E+03
1.61E+03
1.50E+03
1.37E+03
1.23E+03
1.07E+03
9.05E+02
7.22E+02
5.30E+02
3.29E+02
1.22E+02
-8.76E+01
-2.99E+02
-5.08E+02
-7.12E+02
-9.10E+02
-1.10E+03
-1.28E+03
-1.44E+03
-1.59E+03
-1.73E+03
-1.85E+03
-1.95E+03
-2.03E+03
-2.10E+03
-2.15E+03
-2.19E+03
-2.21E+03
-2.21E+03
-2.20E+03
-2.18E+03
-2.15E+03
-2.11E+03
-2.05E+03
-1.99E+03
-1.93E+03
-1.85E+03
-1.78E+03
-1.69E+03
-1.61E+03
-1.52E+03
-1.43E+03
-1.34E+03
-1.25E+03
-1.16E+03
-1.07E+03
-9.85E+02
-8.98E+02
-8.12E+02
-7.27E+02
-6.44E+02
-5.63E+02
-4.84E+02
-4.06E+02
-3.31E+02
-2.57E+02
-1.85E+02
-1.14E+02
-4.54E+01
2.20E+01
8.81E+01
1.53E+02
2.17E+02
2.80E+02
3.42E+02
4.04E+02
4.65E+02
5.27E+02
5.88E+02
6.49E+02
7.10E+02
7.72E+02
8.35E+02
8.98E+02
9.62E+02
1.03E+03
1.09E+03
1.16E+03
1.23E+03
1.30E+03
1.37E+03
1.44E+03
1.51E+03
1.58E+03
1.65E+03
1.72E+03
1.79E+03
1.86E+03
1.93E+03
1.99E+03
2.05E+03
2.10E+03
2.15E+03
2.18E+03
2.21E+03
2.23E+03
2.23E+03
2.22E+03
2.20E+03
2.16E+03
2.09E+03
2.01E+03
1.91E+03
1.79E+03
1.65E+03
1.49E+03
1.32E+03
1.12E+03
9.15E+02
6.94E+02
4.63E+02
2.27E+02
-1.39E+01
-2.54E+02
-4.92E+02
-7.24E+02
-9.46E+02
-1.16E+03
-1.36E+03
-1.54E+03
-1.70E+03
-1.85E+03
-1.98E+03
-2.08E+03
-2.17E+03
-2.24E+03
-2.29E+03
-2.33E+03
-2.34E+03
-2.35E+03
-2.33E+03
-2.30E+03
-2.27E+03
-2.22E+03
-2.16E+03
-2.09E+03
-2.02E+03
-1.94E+03
-1.85E+03
-1.76E+03
-1.67E+03
-1.58E+03
-1.48E+03
-1.39E+03
-1.29E+03
-1.20E+03
-1.10E+03
-1.01E+03
-9.17E+02
-8.26E+02
-7.37E+02
-6.50E+02
-5.65E+02
-4.82E+02
-4.00E+02
-3.21E+02
-2.44E+02
-1.69E+02
-9.49E+01
-2.29E+01
4.76E+01
1.17E+02
1.84E+02
2.51E+02
3.16E+02
3.81E+02
4.45E+02
5.08E+02
5.71E+02
6.33E+02
6.95E+02
7.58E+02
8.20E+02
8.82E+02
9.44E+02
1.01E+03
1.07E+03
1.13E+03
1.20E+03
1.26E+03
1.32E+03
1.38E+03
1.45E+03
1.51E+03
1.57E+03
1.62E+03
1.68E+03
1.73E+03
1.78E+03
1.82E+03
1.86E+03
1.89E+03
1.92E+03
1.93E+03
1.94E+03
1.93E+03
1.91E+03
1.88E+03
1.84E+03
1.78E+03
1.70E+03
1.61E+03
1.50E+03
1.37E+03
1.23E+03
1.07E+03
9.05E+02
7.22E+02
5.30E+02
3.29E+02
1.22E+02
-8.76E+01
-2.99E+02
-5.08E+02
-7.12E+02
-9.10E+02
-1.10E+03
-1.28E+03
-1.44E+03
-1.59E+03
-1.73E+03
-1.85E+03
-1.95E+03
-2.03E+03
-2.10E+03
-2.15E+03
-2.19E+03
-2.21E+03
-2.21E+03
-2.20E+03
-2.18E+03
-2.15E+03
-2.11E+03
-2.05E+03
-1.99E+03
-1.93E+03
-1.85E+03
-1.78E+03
-1.69E+03
-1.61E+03
-1.52E+03
-1.43E+03
-1.34E+03
-1.25E+03
-1.16E+03
-1.07E+03
-9.85E+02
-8.98E+02
-8.12E+02
-7.27E+02
-6.44E+02
-5.63E+02
-4.84E+02
-4.06E+02
-3.31E+02
-2.57E+02
-1.85E+02
-1.14E+02
-4.54E+01
2.20E+01
8.81E+01
1.53E+02
2.17E+02
2.80E+02
3.42E+02
4.04E+02
4.65E+02
5.27E+02
5.88E+02
6.49E+02
7.10E+02
7.72E+02
8.35E+02
8.98E+02
9.62E+02
1.03E+03
1.09E+03
1.16E+03
1.23E+03
1.30E+03
1.37E+03
1.44E+03
1.51E+03
1.58E+03
1.65E+03
1.72E+03
1.79E+03
1.86E+03
1.93E+03
1.99E+03
2.05E+03
2.10E+03
2.15E+03
2.18E+03
2.21E+03
2.23E+03
2.23E+03
2.22E+03
2.20E+03
2.16E+03
2.09E+03
2.01E+03
1.91E+03
1.79E+03
1.65E+03
1.49E+03
1.32E+03
1.12E+03
9.15E+02
6.94E+02
4.63E+02
2.27E+02
-1.39E+01
-2.54E+02
-4.92E+02
-7.24E+02
-9.46E+02
-1.16E+03
-1.36E+03
-1.54E+03
-1.70E+03
-1.85E+03
-1.98E+03
-2.08E+03
-2.17E+03
-2.24E+03
-2.29E+03
-2.33E+03
-2.34E+03
-2.35E+03
-2.33E+03
-2.30E+03
-2.27E+03
-2.22E+03
-2.16E+03
-2.09E+03
-2.02E+03
-1.94E+03
-1.85E+03
-1.76E+03
-1.67E+03
-1.58E+03
-1.48E+03
-1.39E+03
-1.29E+03
-1.20E+03
-1.10E+03
-1.01E+03
-9.17E+02
-8.26E+02
-7.37E+02
-6.50E+02
-5.65E+02
-4.82E+02
-4.00E+02
-3.21E+02
-2.44E+02

'''
d.lower()