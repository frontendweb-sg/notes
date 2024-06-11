#!/bin/bash

echo "Hello world";

text="my name is my pradeep"
: ${text:?"Error"}
echo "I am there"


a=19
b=8

echo "$((a+b))" # plus
echo "$((a-b))" # minus
echo "$((a*b))" # mul
echo "$((a^b))" # div
echo "$((2**3))" # 2*2*2
echo "$((++b))"  #9

run(){
    echo "This is my first function $1"
    return 10
}

run pradeep

value=$?
echo "${value} return value"