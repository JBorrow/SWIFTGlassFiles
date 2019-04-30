#!/bin/bash -l

#SBATCH -J GlassFiles
#SBATCH -N 1
#SBATCH -o make_glass_files.out
#SBATCH -e make_glass_files.err
#SBATCH -p cosma7
#SBATCH -A dp004
#SBATCH --exclusive

#SBATCH -t 48:00:00

bash make_glass.sh
