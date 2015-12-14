##
# Virtual Machine Class
# Class to implement the separation of the indivual VM's for more sophisticated
# error checking and analytics.
# @author David Awad
#

import subprocess


class vm(object):
    '''
    Class to represent a virtual machine and associated information
    '''
    def __init__(self, os, path, vagrantfile='', debug=True):
        self.os = os
        self.path = ''
        self.vagrantfile = vagrantfile
        self.debug = debug
        self.stdout = None
        self.stderr = None

    def boot(self):  # FIXME move this around a bit?
        if self.debug:
            print("DEBUG: Vagrant up on: " + self.os)
            return
        else:
            proc = subprocess.Popen(['vagrant', 'up'],
                                    cwd=self.path,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            # TODO get stderr
            stdout = proc.communicate()[0]

        return
