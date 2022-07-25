# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:25:30 2022

@author: astertaylor
"""

import SAMUS

#create class
standard_class=SAMUS.model("standard_tolerance",a=20,b=50,c=110,mu=10**7)
#runs simulation with only 1 time step per rotation
standard_class.run_model(5,rtol=0.05,data_name='hyperbolic_traj.txt')

#create class
halved_class=SAMUS.model("halved_tolerance",a=20,b=50,c=110,mu=10**7)
#runs simulation with only 1 time step per rotation
halved_class.run_model(5,rtol=0.025,data_name='hyperbolic_traj.txt')
