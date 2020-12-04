#!/bin/bash
docker run -ti \
    -v ${PWD}:/home/lsst/data/ \
    -v /Users/michaelsmith/condorCCD:/opt/lsst/software/stack/stack/current/Linux64/obs_condorCCD \
    lsst:latest
        
