#!/bin/bash

echo "Hello world!"

# System define variables
echo $(env)
echo "------"
echo ${PATH}
echo ${OSTYPE}
echo ${HOSTNAME}
echo ${USER}

ostype=${OSTYPE}
echo "OSTYPE = ${ostype}"

read -p "Enter name" name
echo "name is ${name}"