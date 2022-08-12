# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:25:30 2022

@author: astertaylor

This script is created to demonstrate the validity of the trajectory jump method
used in this code. It runs once with rtol=0.05, and once with rtol=0.025. These
two variations have nearly identical values after the end of the runs,
demonstrating the convergence of this method.
"""

import SAMUS

# create class
standard_class = SAMUS.model("standard_tolerance", a=20, b=50, c=110, mu=10**7)
# runs simulation with only 5 time steps per rotation,
# with a full tolerance
standard_class.run_model(5, rtol=0.05, data_name='hyperbolic_traj')

# create class
halved_class = SAMUS.model("halved_tolerance", a=20, b=50, c=110, mu=10**7)
# runs simulation with only 5 time steps per rotation,
# and with a halved tolerance
halved_class.run_model(5, rtol=0.025, data_name='hyperbolic_traj')
