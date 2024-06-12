#!/bin/bash

echo "Hello World";

# name
read -p "enter name " username;

if [[ ${username,,} == "pradeep" ]]
then
    echo "Welcome back: ${username,,}"
else
    echo "No, match found"
fi

case ${1} in
    pradeep)
        echo "Hello ${username}"
        ;;
    arun)
        echo "Hello ${username}"
        ;;
    sanjeev)
        echo "Hello ${username}"
        ;;
    dilip)
        echo "Hello ${username}"
        ;;
    *)
        echo "No match found ${username}"
        ;;
esac
