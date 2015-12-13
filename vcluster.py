##
# vcluster codebase
# series of functions to manipulate the filesystem and vagrantfiles
# @author David Awad
#

from jinja2 import Environment, FileSystemLoader
from virtual_machine import vm
import subprocess
import shutil
import click
import json
import yaml
import os



env = Environment(loader=FileSystemLoader('templates'))

debug = False


def open_config(config):
    """
    search for and open our config file.
    accepts json or yaml
    """
    if os.path.isfile(config):
        config = yaml.load(open(config))
        if config['debug']:
            print_stderr('Debugging enabled, no virtual machines will be created')
            global debug
            debug = True
        return config
    else:
        print('No settings.yaml found')
        return False


def print_stderr(out):
    print ("\033[91m {}\033[00m".format(out))


def render_template(template_arg, **kwargs):
    """
    This function just uses kwargs to render the vagrantfile template
    using the jinja2 templating engine a la flask usage
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

    return file_paths


def generate_machines(config):
    """
    creates a vm object for each of the operating systems spefied in the
    config file, and adds it to the global list
    """
    load_command = config['command']
    vm_list = []
    for system in config['systems']:
        temp_vagrantfile = render_template('Vagrantfile',
                                           load_os=system,
                                           load_command=load_command,
                                           config=config)

        temp_path = 'temp_cluster/'+system.replace('/', '-')
        os.makedirs(temp_path)  # ex: cluster/vm_trusty64
        with open(temp_path+"/Vagrantfile", "w") as f:
            f.write(temp_vagrantfile)
        # create the new vm object
        temp_vm = vm(system, temp_path, temp_vagrantfile)
        vm_list.append(temp_vm)
    return vm_list


def spin_clusters(vm_list):
    """
    input: Takes in a list of vm Objects
    output: returns

    Iterates through a list of vm objects and performs a vagrant up in a
    subprocess and captures output if it exists
    """
    for vm in vm_list:
        vm.boot()
        if vm.stderr:
            print('Virtual Machine {0} logged to stder:', vm.os)
            print_stderr(vm.stderr)


def clear_vms():
    """
    clear out VM folders
    """
    proc = subprocess.Popen(['rm', '-rf', 'temp_cluster'])
    return


@click.command()
@click.option('--config',
              default='settings.yaml',
              help='The name of your config file, supports YAML and JSON')
def command_line(config):
    """ main thread """
    print_stderr('''WARNING: This kind of unit testing should only be on beefy machines,
     otherwise vagrant may eat your shorts...''')
    # open config file
    config = open_config(config)
    if not config:
        print("config file doesn't exist?")
    # create vagrant files
    vm_list = generate_machines(config)
    # Now spin clusters
    spin_clusters(vm_list)

    # clear_vms()


# start CLI input function using click module
if __name__ == "__main__":
    configs = command_line()
