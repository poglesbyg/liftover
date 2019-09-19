#!/bin/sh

#SBATCH -p general
#SBATCH -N 4 
#SBATCH -t 07-00:00:00
#SBATCH --mem=10g
#SBATCH -n 4

module add anaconda

source activate liftover

python script.py > large_190919v2.out
