# SAMUS
---
Simulator of Asteroid Malformation Under Stress, code for Taylor et al. 2023

---

**setup.py**: Setup file for the package.\
\
**LICENSE.txt**: Text file containing the license for use of this code.

## build
Folder containing the build documents. Auto-generated with pip.

## docs
Folder containing documentation and examples of use.

## SAMUS
Folder containing package itself. 
>**modelFile.py**: Primary file, containing the SAMUS model class. 
>\
>**\_\_init\_\_.py**: Initializing file for the package. 
>
> ### meshes
> Folder containing meshes for use by SAMUS. Users should not have to interact with this. 
>> **\_\_init\_\_.py**: Initializing file for the subpackage. 
>> \
>> **3ball.geo**: GMSH file which contains the simple spherical mesh. Used to create the various improvements.
>> \
>> **3ball?.msh**: GMSH file containing the mesh, which has undergone ? refinements by splitting. 
>> \
>> **3ball?.xml**: xml file containing the mesh, which has undergone ? refinements by splitting. 
>> 
> ### testing
>> **\_\_init\_\_.py**: Initializing file for the subpackage. \
>> \
>> **example\_traj.csv**: csv file with simple, short trajectory information, for use in validations. \
>> \
>> **example\_traj.txt**: txt file with simple, short trajectory information, for use in validations. \
>> \
>> **hyperbolic\_traj.csv**: csv file with hyperbolic trajectory information, for use in validations. \
>> \
>> **hyperbolic\_traj.txt**: txt file with hyperbolic trajectory information, for use in validations. \
>> \
>> **mesh_validation.py**: Python script which runs simulations, validating the use of the lowest-refined mesh via doubling test.\
>> \
>> **modularity_example.py**: Python script which runs simulations and demonstrates the modular use of SAMUS.\
>> \
>> **trajectory_jump_validation.py**: Python script which validates the use of the trajectory jump method via doubling test.
>>
>> ### logs
>> Folder containing the outputs from these testing simulations. 
>>> **coarse\_mesh\_7.txt**: Running log from a coarse-mesh run, run by mesh_validation.py.
>>> \
>>> **Outputs\_coarse\_mesh\_7.csv**: Output lot from from a coarse-mesh run, run by mesh_validation.py.
>>> \
>>> **finer\_mesh\_7.txt**: Running log from a finer-mesh run, run by mesh_validation.py.
>>> \
>>> **Outputs\_finer\_mesh\_7.csv**: Output lot from from a finer-mesh run, run by mesh_validation.py. Compare this file to Outputs\_coarse\_mesh\_7.csv to demonstrate that the mesh usage is validated.
>>> \
>>> **standard\_tolerance\_7.txt**: Running log from a standard-tolerance run, run by trajectory\_jump\_validation.py.
>>> \
>>> **Outputs\_standard\_tolerance\_7.csv**: Output lot from from a standard-tolerance run, run by trajectory\_jump\_validation.py.
>>> \
>>> **halved\_tolerance\_7.txt**: Running log from a halved-tolerance run, run by trajectory\_jump\_validation.py.
>>> \
>>> **Outputs\_halved\_tolerance\_7.csv**: Output lot from from a halved-tolerance run, run by trajectory\_jump\_validation.py. Compare this file to Outputs\_standard\_tolerance\_7.csv to demonstrate that the trajectory jump usage is validated.
>>> 

---
Aster Taylor\
astertaylor@uchicago.edu | aster.taylor8587@gmail.com\
University of Chicago, Department of Astrophysics
