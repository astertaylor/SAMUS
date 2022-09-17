from setuptools import setup

setup(
    name='SAMUS',
    version='0.1.0',
    description='SAMUS package',
    url='https://github.com/astertaylor/SAMUS',
    author='Aster Taylor',
    author_email='astertaylor@uchicago.edu',
    license='BSD 2-clause',
    packages=['SAMUS'],
    install_requires=['numpy',
                      'numpy-quaternion',
                      'pandas',
                      'scipy',
                      'mpi4py',],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
    ],
    package_data={
        'SAMUS': ['meshes/*','examples/*','testing/*']},
    include_package_data=True
)
