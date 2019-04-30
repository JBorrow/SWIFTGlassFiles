for kernel in cubic-spline quintic-spline wendland-C2
do
    mkdir $kernel

    cd $kernel

    for hydro in gadget2 minimal pressure-energy anarchy-pu gizmo-mfm gizmo-mfv
    do
        mkdir $hydro

        cd $hydro

        ../../../configure --with-hydro=$hydro --with-kernel=$kernel --enable-ipo --with-riemann-solver=hllc --disable-hand-vec > configure.log

        make -j > make.log

        cd ..
    done
    
    cd ..
done
