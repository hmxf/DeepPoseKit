#!/bin/bash

arch=`uname -m`

if [ $arch == "aarch64" ]; then
    echo -e "\n# Workaround for DeepPoseKit Error about \"ImportError: /usr/lib/aarch64-linux-gnu/libGLdispatch.so.0: cannot allocate memory in static TLS block\"" >> ~/.bashrc
    echo -e "# This is only for machines with ARM (aarch64) Architecture, this error happens only on ARM machines." >> ~/.bashrc
    echo -e "export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libGLdispatch.so.0" >> ~/.bashrc
fi
