#!/bin/sh

target_port="8080" # set the target port for the local environment. useful if your dev instance has a service already occupying the port
working_directory=`pwd`

docker build -t basic_func .
docker run -p ${target_port}:${target_port} -v "${working_directory}/local:/basic_func" -v "${working_directory}/src:/basic_func/src" -e LOCAL_PORT=${target_port} -it basic_func