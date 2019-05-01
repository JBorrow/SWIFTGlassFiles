# This script creates glass files from the snapshots in the directory.

mkdir glass_files

for hydro in gadget2 minimal pressure-energy anarchy-pu gizmo-mfm gizmo-mfv
do
    for kernel in cubic-spline quintic-spline wendland-C2
    do
        mkdir -p glass_files/$hydro/$kernel

        for npart in 16 32 64 128
        do
            # Find last snapshot
            x="$(ls glass_$npart/$kernel/$hydro | egrep -o '00([0-9]+)' | tail -1)"
            filename=glass_$npart/$kernel/$hydro/uniformBox_$x.hdf5

            cp $filename glass_files/$hydro/$kernel/glassCube_$npart.hdf5
        done
    done
done

