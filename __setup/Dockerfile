FROM ubuntu
MAINTAINER Brian Haas (bhaas@broadinstitute.org)
# with many thanks to Nicolas Delhomme (nicolas.delhomme@slu.se)

RUN apt-get update && apt-get install -y build-essential curl unzip apache2 supervisor \
     default-jre wget git ftp nano python2.7-dev python-pip openssl openssh-server


WORKDIR /usr/local/src


#########
### GateOne SSH interface
#########
RUN git clone https://github.com/liftoff/GateOne/ && \
    cd GateOne && python setup.py install && \
        python run_gateone.py --configure && cd ..






# ports
EXPOSE 22 80 443


# init

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]




RUN apt-get install -y r-base gdebi-core

RUN wget https://download2.rstudio.org/rstudio-server-0.99.903-amd64.deb

RUN gdebi rstudio-server-0.99.903-amd64.deb

RUN apt-get install -y vim emacs


RUN groupadd -g 2000 training && useradd -m -u 2000 -g 2000 training
RUN echo 'training:training' | chpasswd
RUN chsh -s /bin/bash training
RUN echo "alias ll='ls -la -G'" >> /home/training/.profile
RUN usermod -G training,www-data training


