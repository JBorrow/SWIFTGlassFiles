for npart in 32 64 128 256
do
    mkdir glass_$npart
    cd glass_$npart

    for kernel in cubic-spline quintic-spline wendland-C2
    do
        mkdir $kernel
        cd $kernel

        for hydro in gadget2 minimal pressure-energy anarchy-pu gizmo-mfm gizmo-mfv
        do
            mkdir $hydro
            cd $hydro

            python3 ../../../../examples/HydroTests/UniformBox_3D/makeIC.py $npart
            ../../../$kernel/$hydro/examples/swift --hydro --threads=28 ../../../uniformBox.yml

            cd ..
        done
        
        cd ..
    done

    cd ..

done
