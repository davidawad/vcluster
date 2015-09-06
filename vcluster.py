import json
import os
import yaml
from pprint import pprint
from flask import render_template
import shutil

# The purpose of this file is to load the yaml file in memory and pass it
# around to other module around.

def open_configs():
    if os.path.isfile('settings.yml'):
        config = yaml.load(open('settings.yml'))
        return config

    print 'No settings.yml found, reading settings.json'

    with open('settings.json') as data_file:
        data = json.load(data_file)
        return data



def runProcess(exe):
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
      retcode = p.poll() #returns None while subprocess is running
      line = p.stdout.readline()
      yield line
      if(retcode is not None):
        break


def copy_rename(old_file_name, new_file_name):
        src_dir= os.curdir
        dst_dir= os.path.join(os.curdir , "subfolder")
        src_file = os.path.join(src_dir, old_file_name)
        shutil.copy(src_file,dst_dir)

        dst_file = os.path.join(dst_dir, old_file_name)
        new_dst_file_name = os.path.join(dst_dir, new_file_name)
        os.rename(dst_file, new_dst_file_name)


""" for each item in the config array create new vagrantfile , render the template, vagrant up in subprocess and capture stderror if it exists"""

""" render the vagrant file template """
render_template('Vagrantfile', )

if __name__ == "__main__":
    config = open_configs()
    print 'hello'

