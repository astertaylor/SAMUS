# -*- coding: utf-8 -*-
"""
Created on Mon Sep 5 11:39:12 2022

@author: astertaylor

This script is created to demonstrate the validity of the Euler finite-
difference time step used in SAMUS. It runs once with 5 time steps per rotation,
and once with 10 time steps per rotation. These two variations have nearly
identical values after the end of the runs, demonstrating the convergence of
this method.
"""

import SAMUS

#create class
standard_class=SAMUS.model("standard_timestep",a=20,b=50,c=110,mu=10**7)
#runs simulation with only 5 time steps per rotation
standard_class.run_model(5,rtol=0.05,data_name='example_traj')

#create class
halved_class=SAMUS.model("doubled_timestep",a=20,b=50,c=110,mu=10**7)
#runs simulation with 10 time steps per rotation
halved_class.run_model(10,rtol=0.05,data_name='example_traj')
