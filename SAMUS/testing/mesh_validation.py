# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 17:03:40 2022

@author: astertaylor

This script is created to demonstrate the validity of the use of SAMUS's
meshes. We run twice, once with n=0, the default, and once with n=1, which has
~2x the precision. The outputs demonstrate their equivalence, and thus the
convergence of this system.
"""

import SAMUS

# create class
standard_class = SAMUS.model("coarse_mesh", a=20, b=50, c=110, mu=10**7, n=0)
# runs simulation with only 5 time steps per rotation
standard_class.run_model(5, rtol=0.05, data_name='hyperbolic_traj')

# create class
halved_class = SAMUS.model("finer_mesh", a=20, b=50, c=110, mu=10**7, n=1)
# runs simulation with only 5 time steps per rotation
halved_class.run_model(5, rtol=0.05, data_name='hyperbolic_traj')
