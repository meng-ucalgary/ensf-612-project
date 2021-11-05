# dcsn
dCSN is a package for learning Cutset Networks (CNets), a recently introduced tractable Probabilistic Graphical Model.

## Usage

    python dcsn.py nltcs -k 1 -a 0.4

learn a single csn on the nltcs dataset with alpha smoothing parameter
alpha set to 0.4.

    python dcsn.py nltcs -k 5 10 15 20 -a 0.1 0.2 0.3 0.4 -d 10 50 100 -s 2 4 6 

do a grid search for k in {5,10,15,20}, a in {0.1,0.2,0.3,0.4}, d in
{10,50,100} and s in {2,4,6}. Since k is greather than 1 than a
bagging approach is used. Furthermore, by specifying the -r option a
random forest approach may be used.

    python dcsn.py nltcs --al --ap rii 0.75 10 -a 0.5
Learn a single csn using randomised iterative improvement choosing 10 times the best edge to cut with a probability of 0.75.

    python dcsn.py nltcs --al --ap grasp noise 3 0.5 -a 0.5
Learn a single csn using grasp and a noised version of the mutual informations and choosing the best version within 3 attempts.

    python dcsn.py nltcs --al --ap grasp bk 5 4 -a 0.5
Learn a single csn using grasp. While constructing the minimum spanning tree choose a random MI within the best fourths. Do this for 5 times and choose the best performing on the validation set. 

    usage: dcsn.py [-h] [--seed [SEED]] [-o [OUTPUT]] [-r] [--sum] [-k K [K ...]]
               [-d D [D ...]] [-s S [S ...]] [-a ALPHA [ALPHA ...]] [--al]
               [--an] [-v [VERBOSE]] [--ap AP [AP ...]]
               dataset

    positional arguments:
      dataset               Specify a dataset name from data/ (es. nltcs)
    
    optional arguments:
      -h, --help            show this help message and exit
      --seed [SEED]         Seed for the random generator
      -o [OUTPUT], --output [OUTPUT]
                            Output dir path
      -r, --random          Random Forest. If set a Random Forest approach is
                            used.
      --sum                 Use sum nodes.
      -k K [K ...]          Number of components to use. If greater than 1, then a
                            bagging approach is used.
      -d D [D ...]          Min number of instances in a slice to split.
      -s S [S ...]          Min number of features in a slice to split.
      -a ALPHA [ALPHA ...], --alpha ALPHA [ALPHA ...]
                            Smoothing factor for leaf probability estimation
      --al                  Use and nodes as leaves (i.e., CL forests).
      --an                  Use and nodes as inner nodes and leaves (i.e., CL
                            forests).
      -v [VERBOSE], --verbose [VERBOSE]
                            Verbosity level
      --ap AP [AP ...]      Specify the approach to be used to create the forest.
                            First parameter is the approach's name, the others are
                            specific dependent parameters of the chosen
                            approach(ii : Iterative improvement,rii: Randomised Iterative improvement )


## Copyright (C) 2017

    Nicola Di Mauro, Antonio Vergari, Claudio Mastronardo
    Department of Computer Science 
    University of Bari, Bari, Italy 

This file is part of dCSN.
    
dCSN is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation (version 2).

dCSN is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not,
see [http://www.gnu.org/licenses/](http://www.gnu.org/licenses/) 

