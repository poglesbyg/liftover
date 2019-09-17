#!/bin/sh

#SBATCH -p general
#SBATCH -N 4 
#SBATCH -t 07-00:00:00
#SBATCH --mem=10g
#SBATCH -n 4

module load anaconda

source activate liftover
which python3 
conda install biopython -y

python3 script.py > large_19917v4.out
