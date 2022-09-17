# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:56:54 2022

@author: Aster Taylor

This script provides a demonstration of how to add functions to the SAMUS class
which provide data outputs. All functions must either take no inputs or take
'self', and use class variables. This script provides examples of both, and
uses multiple data types.

"""
import SAMUS

# defines function which doesn't use class variables
def test_func():
    return([1, "test"], ["ones", "string"])

# defines function which uses class variables, returning the viscosity
def get_viscosity(self):
    return(float(self.mu), "Viscosity")


# create class
mod_class = SAMUS.model("modularity_example", mu=10**6)

# runs simulation for a brief period with only 1 time step per rotation
frame,_ = mod_class.run_model(1, data_name='example_traj',
                            funcs=['moment_of_inertia', 'princ_axes',
                                   test_func, get_viscosity])

# prints DataFrame as demonstration
print("Frame:",frame)
