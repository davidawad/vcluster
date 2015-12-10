##
# Virtual Machine Class
# Class to implement the separation of the indivual VM's for more sophisticated
# error checking and analytics.
# @author David Awad
#


class vm:

    __init__(self, os):
        # OS of the virtual machine
        self.os = os
        self.vagrantfile = ''
        self.stdout = ''
        self.stderr = ''
