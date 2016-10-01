FROM rocker/rstudio
MAINTAINER Brian Haas (bhaas@broadinstitute.org)

## install bioconductor packages:
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R");library(BiocInstaller); biocLite("edgeR", dep = TRUE)'



# ports
EXPOSE 8787
