#!/bin/sh

#SBATCH -p general
#SBATCH -N 4 
#SBATCH -t 07-00:00:00
#SBATCH --mem=10g
#SBATCH -n 4

module load anaconda

source activate liftover
which python 

python script.py > large_19918v1.out
