FROM rocker/rstudio
MAINTAINER Tim Tickle (ttickle@broadinstitute.org) and Brian Haas (bhaas@broadinstitute.org)

######################
## Environment
######################

### locations
ENV BIN /usr/local/bin
ENV DATA /usr/local/data
ENV SRC /usr/local/src

######################
## Dependencies and Tools
######################
##############
## Helper tools
RUN apt-get update && \
    apt-get install -y unzip wget git \
    r-base r-base-dev \
    libssl-dev libcurl4-openssl-dev libxml2-dev libxt-dev libgstreamer0.10-0 libjpeg62 ibgstreamer-plugins-base0.10-0 \
    libcairo2-dev


##############
## devtools
## scone
## seurat
## RaceID
## FastProject
## scater
RUN echo "source(\"https://bioconductor.org/biocLite.R\")" > ${SRC}/install_pkgs.R && \
    echo "biocLite(\"devtools\")" >> ${SRC}/install_pkgs.R && \
    echo "biocLite()" >> ${SRC}/install_pkgs.R && \
    echo "biocLite(\"YosefLab/scone\", dependencies=TRUE)" >> ${SRC}/install_pkgs.R && \
    echo "devtools::install_github(\"satijalab/seurat\")" >> ${SRC}/install_pkgs.R && \
    echo "biocLite(c(\"RcppArmadillo\", \"Rook\", \"rjson\", \"RMTstat\", \"extRemes\", \"pcaMethods\", \"Cairo\"), dependencies=TRUE)" >> ${SRC}/install_pkgs.R && \
    echo "biocLite(c(\"pheatmap\", \"amap\", \"useful\"), dependencies=TRUE)" >> ${SRC}/install_pkgs.R && \
    echo "biocLite(c(\"scater\"), dependencies=TRUE)" >> ${SRC}/install_pkgs.R && \
    echo "biocLite(c(\"org.Hs.eg.db\"), dependencies=TRUE)" >> ${SRC}/install_pkgs.R && \
    echo "biocLite()" >> ${SRC}/install_pkgs.R
    
Run Rscript ${SRC}/install_pkgs.R

WORKDIR ${SRC}
RUN wget https://github.com/hms-dbmi/scde/archive/1.99.1.tar.gz && \
    R CMD INSTALL 1.99.1.tar.gz
    
## RStudio
RUN wget https://download1.rstudio.org/rstudio-0.99.903-amd64.deb && \
    dpkg -i rstudio-0.99.903-amd64.deb


# ports
EXPOSE 8787
