Options for packaging code - Comparison
=======================================
There are multiple ways to package and distribute a Python program.

.. csv-table:: Comparison chart (--> increase in content from left to right)
    :file: _table/packaging.csv
    :header-rows: 1

Notes
-----
PEX (and others)
````````````````
* Tools built around zipapp (part of Python standard library)
* Zipapp … no C extensions supported
* These tools come from big companies (Google, Facebook, Linkedin)
* A \*.pex file is a complete virtual environment contains all required packages
* A \*.pex file can be used standalone without installing it into a different environment

System Packages
```````````````
* RPM: Red Hat Package Manager
* DEB: Debian Package Manager
* System administrator approach
* Considered more stable to depend on system packages than python libraries

Conda
`````
* Many PyPi packages are available as Conda package
* Community project
* Makers of conda distribution usually are not the developers

Containers / Docker
```````````````````
* Suitable if application requires a very specific OS setup
* Don’t use alpine OS for deploying Python apps, standard C interpreter is
  not well suited for Python (should always use glibc, but Alpine uses msl)
* Installing binary wheels is disabled in alpine (since binary compatibility
  is not given); compiling source code works mostly, though
* Choose Debian image to ensure that pip installs works on your container
* Upgrading alpine to properly compile a library (e.g. pandas) takes a lot
  of tools (installation time about 15 minutes)

.. csv-table:: General recommendations
    :file: _table/packaging_good_bad.csv
    :header-rows: 1
    :stub-columns: 1

Links
-----
PEX (and others):

* https://github.com/pantsbuild/pex
* https://github.com/google/subpar
* https://github.com/linkedin/shiv/
* https://docs.python.org/3/library/zipapp.html

Conda:

* https://conda-forge.org/
* https://anaconda.org/anaconda/repo

Docker:

* https://www.gnu.org/software/libc/
* https://musl.libc.org/
* https://hub.docker.com/_/alpine
* https://hub.docker.com/_/debian

Sources
```````
* https://realpython.com/podcasts/rpp/24/
* https://pythonspeed.com/articles/distributing-software/