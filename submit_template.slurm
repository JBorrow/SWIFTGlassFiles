#!/bin/bash -l

#SBATCH -J HYDRO-KERNEL-NP-GlassFiles
#SBATCH -N 1
#SBATCH -o make_glass_files.out
#SBATCH -e make_glass_files.err
#SBATCH -p cosma7
#SBATCH -A dp004
#SBATCH --exclusive

#SBATCH -t 48:00:00

python3 ../../../../examples/HydroTests/UniformBox_3D/makeIC.py NP
../../../KERNEL/HYDRO/examples/swift --hydro --threads=28 ../../../uniformBox.yml
