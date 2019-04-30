for npart in 16 128 256
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

            cp ../../../submit_template.slurm ./submit.slurm
            sed -i "s/HYDRO/${hydro}/g" submit.slurm
            sed -i "s/NP/${npart}/g" submit.slurm
            sed -i "s/KERNEL/${kernel}/g" submit.slurm

            sbatch submit.slurm

            cd ..
        done
        
        cd ..
    done

    cd ..

done
