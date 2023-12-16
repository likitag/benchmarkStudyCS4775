# Steps to Reproduce Benchmark Study

## Clone this repository
## Install required libraries for algorithms 
### Install Clustal Omega 
1. Download the Source code .tar.gz : http://www.clustal.org/omega/
2. follow the steps in this install file: http://www.clustal.org/omega/INSTALL
### Install KAlign
1. follow the installation steps here: https://github.com/TimoLassmann/kalign
### Install MAFFT 
1. follow the installation steps here: https://mafft.cbrc.jp/alignment/software/
### Install MUSCLE
1. follow the installation steps here: https://github.com/rcedgar/muscle?tab=readme-ov-file


## Modify the paths in the algorithm 
in the run_msa function, ensure that you modify the paths for each algorithms to your respective path based on where you have installed tha algorithm and its required libraries

## Run the benchmark algorithm
cd into the benchmarkStudyCS4775 folder and run the following terminald command: python3 benchmark.py

## Check results 
Results of the benchmark study will be written to the results.txt file

