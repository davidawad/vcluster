import json
import os
import yaml
from pprint import pprint
import shutil
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))


def open_configs():
    if os.path.isfile('settings.yaml'):
        config = yaml.load(open('settings.yaml'))
        return config

    print 'No settings.yaml found, reading settings.json'

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

def render_template(template_arg, **kwargs):
    template = env.get_template(template_arg)
    output_from_parsed_template = template.render(kwargs)
    return output_from_parsed_template

""" for each item in the config array create new vagrantfile , render the template, vagrant up in subprocess and capture stderror if it exists"""

""" render the vagrant file template """
# render_template('Vagrantfile', )

if __name__ == "__main__":
    config = open_configs()
    i = 0
    load_command = config['command']
    for system in config['systems']:
        print system
        print render_template('Vagrantfile',
                                load_os=system,
                                load_command=load_command)
        # copy_rename('templates/Vagrantfile', 'templates/Vagrantfile')


