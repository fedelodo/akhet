FROM akhet/images/ubuntu-16-04-gnome-root6:latest

# build commands
RUN wget http://geant4.cern.ch/support/source/geant4.10.03.p01.tar.gz && \
    tar zxvf geant4.10.03.p01.tar.gz && rm /geant4.10.03.p01.tar.gz && \
    mkdir /geant4-build && cd /geant4-build && \
    cmake -DGEANT4_BUILD_MULTITHREADED=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/geant4.10.02 \
        -DGEANT4_INSTALL_DATA=ON \
        -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_QT=ON -DGEANT4_USE_XM=ON \
        -DGEANT4_USE_GDML=ON \
        /geant4.10.03.p01/ && \
    make -j 4 && make install && \
    mv /geant4-build/CMakeCache.txt /opt/geant4.10.02/ && \
    rm -rf /geant4-build && rm -rf /geant4.10.03.p01
RUN echo source /opt/geant4.10.02/bin/geant4.sh  >> /etc/bash.bashrc
