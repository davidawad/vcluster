from jinja2 import Environment, FileSystemLoader
from pprint import pprint
import shutil
import json
import yaml
import os
import subprocess
import click

##
# vcluster codebase
# series of functions to manipulate the filesystem and vagrantfiles
#
#

env = Environment(loader=FileSystemLoader('templates'))


def test_command(command):
    """
    The command
    """
    cmd = command.split(' ')
    print "RUNNING COMMAND FOR " + str(command)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    stdout = proc.communicate()[0]
    myList = []
    print stdout
    return stdout


def copy_rename(old_file_name, new_file_name):
        """
        create a copy of an old file and create a new
        copy with the given name.
        """
        src_dir = os.curdir
        dst_dir = os.path.join(os.curdir, "subfolder")
        src_file = os.path.join(src_dir, old_file_name)
        shutil.copy(src_file, dst_dir)

        dst_file = os.path.join(dst_dir, old_file_name)
        new_dst_file_name = os.path.join(dst_dir, new_file_name)
        os.rename(dst_file, new_dst_file_name)


def render_template(template_arg, **kwargs):
    """
    This function just uses kwargs to render the vagrantfile template
    using the jinja2 templating engine
    """
    template = env.get_template(template_arg)
    output_from_parsed_template = template.render(kwargs)
    return output_from_parsed_template


def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames). We're traversing the
    temp directory to find the vagrantfiles for each of the vms
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.


# TODO add functionality for taking config on command line
def open_configs(filename):
    """
    search for and open our config file.
    accepts json or yaml
    """
    if os.path.isfile(filename):
        config = yaml.load(open(filename))
        return config

    print 'No settings.yaml found, reading settings.json'

    with open(filename) as data_file:
        data = json.load(data_file)
        return data


def generate_vagrant(config):
    i = 0
    load_command = config['command']
    for system in config['systems']:
        """ for each item in the config array create a new vagrantfile , render the
        template"""
        vagrantfile = render_template('Vagrantfile',
                                      load_os=system,
                                      load_command=load_command
                                      )
        # print vagrantfile
        curr_direc = 'temp/vm_'+str(i)
        os.makedirs(curr_direc)
        with open(curr_direc+"/Vagrantfile", "w") as text_file:
            text_file.write(vagrantfile)
        i += 1
    """ Now done generating vagrant files, generate the subprocesses"""
    spin_clusters()


def spin_clusters():
    """
    vagrant up in a subprocess and capture output if it exists
    """
    vms = get_filepaths('temp')
    i = 0
    for vFile in vms:
        test_command('./run_vm.sh ' + str(i))
        i += 1


@click.command()
@click.option('--config',
              default='settings.yaml',
              help='The name of your config file, supports YAML and JSON')
def command_line(config):
    """
    search for and open our config file.
    accepts json or yaml
    """
    if os.path.isfile(config):
        config = yaml.load(open(config))
        generate_vagrant(config)

    # TODO better design for accepting json
    '''
    with open(config) as data_file:
        data = json.load(data_file)
        return data
    '''

if __name__ == "__main__":
    configs = command_line()
