#FairSoft

This repository contain the installation routines of all the external software needed 
to compile and use FairRoot.
To simplify the installation procedure of all these packages we provide a set of 
scripts which will automatically download, unpack, configure, build‚ and install 
all packages.

The scripts work on most Linux flavors and on Mac OSX. If you encounter any problems 
please create an issue at https://github.com/FairRootGroup/FairSoft/issues.

##Prerequisites

The script needs a complete build environment to compile all the source code. A list
of all needed system packages can be found in the DEPENDENCIES file. All these system
packages are installed using the package manager of the used Linux flavor. A list of
complete command lines to install all packages in one go are also added in the
DEPENDENCIES file, so one only has to cut-n-paste the appropriate command line to a
terminal window and start the installation.

##Guided Installation 

To start the installation procedure one has to run the configure.sh script which is
found in the main directory of FairSoft from within this directory. If the script is
called without parameters one is guided through some menus to choose the appropriate
setup.

  FairSoft> ./configure.sh

In the first menu one has to define the compiler which should be used for the
installation. The normal choices would be _gcc_ for Linux and _Clang_ for Mac OSX.
The compiler must be installed on the system. If one choose a compiler which is not
installed, the installation procedure will stop when checking for the prerequisites
defined above.

In the second menu one has to decide if the packages should be installed in
debug, normal or optimization mode. If one choose the optimization mode one
should also define the correct optimization flags in the file
scripts/check_system.sh, even if there are some default settings.
If unsure don't use the optimization option.

In the third menu one has to define if one need to install all packages to
run a simulation. If unsure choose _Yes_.

If the previous choice was _Yes_ one has to define in the next menu how to handle the 
Geant4 data files. These files have after installation a size of approximately 650 MB. 
If you don't intent to use Geant4 you should choose _Don't install_, if unsure choose
one of the other options described below. 

If the data files should be installed it is normally save to choose the
option Internet which will download the files and does the installation
automatically when installing Geant4. 
Only if your system cannot download the files choose the Directory option. 
In this case one has to put the files into the transport directory so that they can be 
installed. One can download the files from the following webpage.

http://geant4.cern.ch/support/download.shtml

In the next menu one has to decide if the python bindings for Geant4 and Root should
be installed. If unsure choose _No_.

In the last menu one has to define the installation directory. All the programs will be
installed into this directory. One shouldn't use as installation directory a directory 
with is used by the system (e.g. /usr or /usr/local). Since it is possible to install 
several version of "FairSoft" in parallel it is advisable to use a name tag in the 
directory name (e.g. <install_dir>/fairsoft_dec13)

After passing all menus the installation process will check if all needed system
packages are installed. If one or more packages are missing the installation process
will stop with an detailed error message. In this case please install the missing
system packages and start the installation again.

The installation procedure may take a long time depending on your computer. If the
installation procedure stops with an error it is save to start the script again.
It will check which packages have been already compilled and installed successfully
and will skip these packages.

##Installation with configuration file

As an alternative for experienced users it is also possible to pass an input file to
the script which defines all the needed information. The configure.sh script will
check if all variables are defined in the input file and if the values are allowed.
In case an error is found the script will stop with an error message. Three example
files (automatic.conf, grid.conf, and recoonly.conf) can be found in the main 
directory of FairSoft. 

##Included Packages

* cmake 2.8.12.2 (only installed if installed version is to old)
* gtest  1.7.0
* gsl 1.16
* boost 1_54_0
* Pythia6 416
* HepMC 2.06.09
* Pythia8 183
* Geant4 10.00.p01
* ROOT v5.34.19
* Pluto v5.37
* Geant321+_vmc 1.15a
* VGM v3-06
* G4VMC 2.15
* MillePede V04-01-01
* ZeroMQ 3.2.4
* Protocoll Buffers 2.5.0
* Nano Message  0.4-beta

##Installation of ALFA (Alice-FAIR software)

The ALFA installation will install the FairSoft as above and after that it will install
three more packages:

* FairRoot 
* DDS
* AliRoot

  FairSoft> ./alfaconfig.sh

The script will get the source code of all the packages from there own repostories, 
compile and install tme. The versions and the urls of the different repostories used
are specified in the file "scripts/package_versions.sh" 





