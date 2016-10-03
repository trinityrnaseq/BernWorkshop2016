#!/usr/bin/env python
# encoding: utf-8

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import os, sys, re
import logging
import argparse
import subprocess

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger(__name__)



def main():

    parser = argparse.ArgumentParser(description="instantiate user spaces", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("--num_users", type=str, default="", required=True, help="number of users")
    parser.add_argument("--ip_addr", type=str, required=True, help="IP address for server")


    parser.add_argument("--apache_base_port", type=int, default=8001, help="base port for apache")
    parser.add_argument("--gateone_base_port", type=int, default=9001, help="base port for gateone")
    parser.add_argument("--rstudio_base_port", type=int, default=10001, help="base port for rstudio")

    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)      
    

    apache_user_port = args.apache_base_port
    gateone_user_port = args.gateone_base_port
    rstudio_user_port = args.rstudio_base_port

    users_basedir = os.path.abspath("user_spaces")
    os.makedirs(users_basedir)

    for i in range(0, args.num_users):

        # create user directory
        user = "user_{:02d}".format(i)
        user_dir = os.path.sep.join([users_basedir, user])
        os.makedirs(user_dir)

        # launch docker
        cmd = str("docker run --rm -ti -v {}:{} " +
                  " -v /shared:/shared:r " +
                  " -p {}:80 -p {}:443 " +
                  " --name trinity_{} -d bernws2016/trinity".format("/home/training", user_dir,
                                                                    apache_user_port,
                                                                    gateone_user_port,
                                                                    user))

        subprocess.check_output(cmd)
        
        apache_user_port += 1
        gateone_user_port += 1
        rstudio_user_port += 1



    sys.exit(0)
 
####################
 
if __name__ == "__main__":
    main()
