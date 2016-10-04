# BernWorkshop2016
workshop in Bern, Switzerland in Oct 2016

trinity ws materials:
*  ftp'd data from Broad as: trinity_docker_workshop_shared.tar.gz
*  git clone https://github.com/trinityrnaseq/BernWorkshop2016.git

single cell ws materials:
*  git clone https://github.com/TimothyTickle/single_cell_analysis.git


##
setup:

   sudo groupadd -g 2000 training
   sudo useradd -m -u 2000 -g 2000 training
   echo 'training:training' | sudo chpasswd
   sudo usermod -G training,www-data training
   sudo chsh training -s /bin/bash


Load trinity workshop docker
   
   zcat bernws2016-trinity.tar.gz | docker load
   # can't distribute due to unfortunate licensing issues.


## prep shared folders under /home/training

    sudo mv trinity_docker_workshop_shared.tar.gz /home/training
    su training
    cd $HOME
    tar xvf trinity_docker_workshop_shared.tar.gz
    exit



