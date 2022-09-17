# SAMUS
---
Simulator of Asteroid Malformation Under Stress, package designed for Taylor et al. 2022. Questions on its use should be directed to astertaylor@uchicago.edu.

This code simulates the deformation of minor bodies, assuming that they are homogenous incompressible fluid masses. They are initialized as ellipsoids and the Navier-Stokes equations are interatively solved to investigate the deformation of the body over time. This package is highly modular, and allows for user-defined output functions, size, and trajectories. 

SAMUS is structured as a single large class, which allows for variables to be stored and for arbitrary function calls. A single high-fidelity simulation run can be quite lengthy, and so this allows for ease of debugging and investigation. It utilizes Python3.8 and above, and depends on the `numpy`, `FEniCS`, `DOLFIN`, `UFL`, `SciPy`, `pandas`, `quaternion`, and `mpipy` packages. 

Further description of SAMUS can be found in Taylor et al. 2022 (found on the ArXiv here (LINK)) and in the in-line documentation.

Examples of SAMUS's use are given in the **examples** folder. 

## Installation
There are two primary methods of installing SAMUS:
1) Install through the Python Package Index (PyPI):\
`pip install SAMUS`
2) Install the developer's version on GitHub:\
`git clone https://github.com/astertaylor/SAMUS`\
`cd SAMUS`\
`python setup.py install` (Note that this command may require a `sudo` instruction.)


SAMUS File Tree
---

**setup.py**: Setup file for the package.\
\
**LICENSE.txt**: Text file containing the license for use of this code.\
\
**README.md**: Markdown file with basic documentation.

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
>> **example\_traj.txt**: txt file with simple, short trajectory information, for use in validations. \
>> \
>> **hyperbolic\_traj.csv**: csv file with hyperbolic trajectory information, for use in validations. \
>> **hyperbolic\_traj.txt**: txt file with hyperbolic trajectory information, for use in validations. \
>> \
>> **mesh_validation.py**: Python script which runs simulations, validating the use of the lowest-refined mesh via doubling test.\
>> \
>> **modularity_example.py**: Python script which runs simulations and demonstrates the modular use of SAMUS.\
>> \
>> **trajectory_jump_validation.py**: Python script which validates the use of the trajectory jump method via doubling test.\
>> \
>> **euler_step_validation.py**: Python script which validates the use of Euler finite-difference time steps via a doubling test.
>>
>> ### logs
>> Folder containing the outputs from these testing simulations. 
>>> **coarse\_mesh\_7.txt**: Running log from a coarse-mesh run, run by mesh_validation.py.\
>>> **Outputs\_coarse\_mesh\_7.csv**: Output lot from from a coarse-mesh run, run by mesh_validation.py.\
>>> \
>>> **finer\_mesh\_7.txt**: Running log from a finer-mesh run, run by mesh_validation.py.\
>>> **Outputs\_finer\_mesh\_7.csv**: Output lot from from a finer-mesh run, run by mesh_validation.py. Compare this file to Outputs_coarse_mesh_7.csv to demonstrate that the mesh usage is validated.\
>>> \
>>> **standard\_tolerance\_7.txt**: Running log from a standard-tolerance run, run by trajectory\_jump\_validation.py.\
>>> **Outputs\_standard\_tolerance\_7.csv**: Output lot from from a standard-tolerance run, run by trajectory\_jump\_validation.py.\
>>> \
>>> **halved\_tolerance\_7.txt**: Running log from a halved-tolerance run, run by trajectory\_jump\_validation.py.\
>>> **Outputs\_halved\_tolerance\_7.csv**: Output lot from from a halved-tolerance run, run by trajectory\_jump\_validation.py. Compare this file to Outputs\_standard\_tolerance\_7.csv to demonstrate that the trajectory jump usage is validated.\
>>> \
>>> **standard\_timestep\_7.txt**: Running log from a standard-timestep run, run by euler\_step\_validation.py.\
>>> **Outputs\_standard\_timestep\_7.csv**: Output lot from from a standard-tolerance run, run by euler\_step\_validation.py.\
>>> \
>>> **doubled\_timestep\_7.txt**: Running log from a double-timestep run, run by euler\_step\_validation.py.\
>>> **Outputs\_doubled\_timestep\_7.csv**: Output lot from from a double-timestep run, run by euler\_step\_validation.py. Compare this file to Outputs\_standard\_timestep\_7.csv to demonstrate that the usage of a Euler finite-difference timestep is validated.\

> ### examples
> Folder containing examples of `SAMUS`'s use. There are .ipynb and .py files for both examples. The .ipynb files have greater documentation, and the `.py` files are more efficient to run. 
>> **example\_traj.csv**: .csv file with simple, short trajectory information, for use in validations. \
>> **example\_traj.txt**: .txt file with simple, short trajectory information, for use in validations. \
>> \
>> **Basic\_Usage\_Example.ipynb**: A Jupyter Notebook file with a very basic example of `SAMUS`'s use. This file has relatively extensive documentation, and should be used to gain greater understanding of how `SAMUS` works. \
>> **basic\_usage\_example.py**: A Python script with a very basic example of `SAMUS`'s use. This file should be run by the learner, as it is capable of being run with `mpirun` and runs significantly faster than the corresponding .ipynb file. \
>> \
>> **Modularity\_Example.ipynb**: A Jupyter Notebook file with an example of `SAMUS`'s modular functionalities. This file has relatively extensive documentation, and should be used to gain greater understanding of how `SAMUS` works. \
>> **modularity\_example.py**: A Python script with an example of `SAMUS`'s modular functionalities. This file should be run by the learner, as it is capable of being run with `mpirun` and runs significantly faster than the corresponding .ipynb file. \

---
Aster Taylor\
astertaylor@uchicago.edu | aster.taylor8587@gmail.com\
University of Chicago, Department of Astrophysics
