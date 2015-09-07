#!/bin/bash

echo "running vm $1"

cd temp/vm_$1

echo "--------------------"

cat Vagrantfile

# WARNING unittest on beefy machines
echo "creating VM..."

echo "vagrant up"
# vagrant up
