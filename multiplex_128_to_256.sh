# This script creates glass files from the snapshots in the directory.

mkdir glass_files

for hydro in gadget2 minimal pressure-energy anarchy-pu gizmo-mfm gizmo-mfv
do
    echo "Multiplexing ${hydro}"
    for kernel in cubic-spline quintic-spline wendland-C2
    do
        filename_in=glass_files/$hydro/$kernel/glassCube_128.hdf5
        filename_out=glass_files/$hydro/$kernel/glassCube_256.hdf5

        python3 multiplex_glass_file.py -i $filename_in -o $filename_out
    done
done

