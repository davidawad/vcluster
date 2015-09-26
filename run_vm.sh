#!/bin/bash

echo "running vm $1"

cd temp/vm_$1

echo "--------------------"

# WARNING unittest on beefy machines
echo "creating VM..."

# currently commented for CLI dev
# vagrant up

if [ $2 == "debug" ]
    then
    echo "DEBUGGING IN SCRIPT! \n"
    cat Vagrantfile
else
    echo "vagrant up for vm $1" +
fi
