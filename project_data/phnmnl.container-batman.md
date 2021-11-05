![Logo](BATMAN_logo.gif)

# BATMAN
Version: 1.2.12.0

## Short Description

Bayesian Automated Metabolite Analyser for NMR spectra (BATMAN).

## Description

BATMAN: open source software for batch metabolites NMR resonance peak fitting.

BATMAN deconvolves resonance peaks from NMR spectra of complex mixtures and obtains concentration estimates for the corresponding metabolites automatically. This is achieved through a database of spectral profiles for known metabolites and a Bayesian Markov Chain Monte Carlo algorithm.

Users have the options to specify the multiplet ppm position, position shift range, peak width range and so on. Parallel processing is available if processing several spectra. The installation and testing instructions can be found at:
http://batman.r-forge.r-project.org/.

## Key features

- NMR Processing

## Functionality

- Annotation / NMR
- Post-processing

## Approaches

- Metabolomics / Targeted

## Instrument Data Types

- NMR / 1D NMR

## Screenshots

Screen shots obtained from the original BATMAN page.

## Tool Authors

- Jie Hao (Imperial College London)
- William Astle
- Maria De Iorio (University College London)
- Timothy Ebbels (Imperial College London)

## Container Contributors

- [Jianliang Gao](https://github.com/jianlianggao) (Imperial College London) 
- [Pablo Moreno](https://github.com/pcm32) (EMBL-EBI)

## Website

- http://batman.r-forge.r-project.org/


## Git Repository

- https://github.com/phnmnl/container-batman.git

## Installation

This tool is preloaded in PhenoMeNal Galaxy deployments. 

For local individual installation:

```bash
docker pull container-registry.phenomenal-h2020.eu/phnmnl/batman
```

## Usage Instructions

Available on PhenoMeNal Galaxy instances under PhenoMeNal H2020 Tools -> NMR.

For direct docker usage:

```bash
docker run -v $PWD:/data container-registry.phenomenal-h2020.eu/phnmnl/batman -i /data/nmr_spectra_input.txt -o /data -p /data/batman_options.txt -u /data/multi_data_user.csv -l /data/metabolitesList.csv
```

## Publications
- Hao, J., et al.,  Bayesian deconvolution and quantification of metabolites in complex 1D NMR spectra using BATMAN. Nature Protocols. 2014. 9 (6): pp 1416-1427. DOI: 10.1038/nprot.2014.090. http://www.nature.com/nprot/journal/v9/n6/full/nprot.2014.090.html
- Liebeke, M., et al., Combining Spectral Ordering with Peak Fitting for One-Dimensional NMR Quantitative Metabolomics. Analytical Chemistry, 2013. 85 (9): pp 4605–4612. DOI: 10.1021/ac400237w. http://pubs.acs.org/doi/abs/10.1021/ac400237w
- Hao, J., et al., BATMAN¨Can R package for the automated quantification of metabolites from nuclear magnetic resonance spectra using a Bayesian model. Bioinformatics, 2012. 28 (15): pp 2088-90. http://bioinformatics.oxfordjournals.org/content/28/15/2088
- Astle, W., et al., A Bayesian Model of NMR Spectra for the Deconvolution and Quantification of Metabolites in Complex Biological Mixtures. Journal of the American Statistical Association, 2012. 107(500): pp 1259-1271. http://www.tandfonline.com/doi/abs/10.1080/01621459.2012.695661#.UgEf-hbZa4k.
