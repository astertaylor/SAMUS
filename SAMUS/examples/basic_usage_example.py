# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 21:22:42 2022

This is a basic example of the usage of SAMUS for asteroid simulations. It simulates an ellipsoid of size 100:100:50, on a short trajectory given by example_traj.csv.

The Jupyter Notebook Basic_Usage_Example.ipynb contains further comments on this code, for which this is a script.

It is recommended that you run this script with the command `mpirun -n 1 python3 basic_usage_example.py`.

@author: aster
"""

# Firstly, we import the necessary packages for this example.

import SAMUS

# Now, we set several parameters for the model.

rho = 0.5 # density, g/cm^3

p = 10 # period, hours

n = 0 # number of mesh refinements. Increasing this number significantly slows the computations.

omega = [1,0,1] #rotation axis, which need not be normalized

mu = 10**6 # dynamic viscosity, poise

a = 100 # meters
b = 100 # meters
c = 50 # meters

# Now we create the class object which will store the model, which we name "example".

sim_object = SAMUS.model("basic_example", a=a, b=b, c=c, mu=mu, rho=rho,
                         omegavec=omega, szscale=2, n=n)

# Now we run the model.

frame, div = sim_object.run_model(nsrot=10, # number of steps per rotation
                                 rtol=0.01, # setting a tolerance of 1%
                                 period=p, # using a period of 10 hours
                                 Cmax=1, # setting the CFL criterion to 1
                                 savesteps=False, # no models of intermediate steps
                                 data_name="example_traj", # name of the csv file holding the trajectory data
                                 funcs=['moment_of_inertia','princ_axes']) # functions for use in the output

# We print the outputs.

print("\'frame\' type:",type(frame))
print(frame)
print("\'div\' type:",type(div),"\'div\' value:",div)

# Finally, we reset the simulation to its original position.

sim_object.reset_model()
