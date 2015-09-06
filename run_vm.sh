#!/bin/bash


# echo "the $1 eats a $2 every time there is a $3"
# echo "bye:-)"

#the dog eats a bone every time there is a moose
# bye :)

echo "running vm $1"

cd temp/vm_$1

echo "--------------------"

cat Vagrantfile

# TODO unittest on beefy machines
# vagrant up
