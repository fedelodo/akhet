FROM akhet/images/ubuntu-16-04-plasma-cpp:latest

RUN wget https://root.cern.ch/download/root_v6.09.02.source.tar.gz && \
    tar zxvf root_v6.09.02.source.tar.gz && \
    rm /root_v6.09.02.source.tar.gz && mkdir /root-build && cd /root-build && \
    cmake -DPYTHON_EXECUTABLE=/usr/bin/python2.7 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython2.7.so \
        -DCMAKE_INSTALL_PREFIX=/opt/root_v6.09.02 \
        ../root-6.09.02/ && \
    make -j 4 && make install && \
    rm -rf /root-build && rm -rf /root-6.09.02
RUN echo source /opt/root_v6.09.02/bin/thisroot.sh  >> /etc/bash.bashrc
