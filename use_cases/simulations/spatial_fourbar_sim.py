# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:47:07 2019

@author: khaled.ghobashy
"""
import numpy as np
import matplotlib.pyplot as plt

from source import pkg_path
from source.solvers.python_solver import solver

import use_cases.generated_templates.assemblies.spatial_fourbar_assm as assm
from use_cases.generated_templates.configurations import spatial_fourbar_cfg

assm.FB.config = spatial_fourbar_cfg.configuration()
assm.FB.config.load_from_csv(pkg_path + r'\use_cases\generated_templates\configurations\csv_files\spatial_fourbar_mod.csv')

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
