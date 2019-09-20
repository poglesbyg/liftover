#!/bin/sh

#SBATCH -p general
#SBATCH -N 1
#SBATCH -t 1:00:00
#SBATCH --mem=4G
#SBATCH -n 1

module add anaconda
source activate julia
which julia
julia script.jl 
