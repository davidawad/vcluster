from jinja2 import Environment, FileSystemLoader
from pprint import pprint
import shutil
import json
import yaml
import os


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
      retcode = p.poll()  # returns None while subprocess is running
      line = p.stdout.readline()
      yield line
      if(retcode is not None):
        break


def copy_rename(old_file_name, new_file_name):
        src_dir = os.curdir
        dst_dir = os.path.join(os.curdir, "subfolder")
        src_file = os.path.join(src_dir, old_file_name)
        shutil.copy(src_file, dst_dir)

        dst_file = os.path.join(dst_dir, old_file_name)
        new_dst_file_name = os.path.join(dst_dir, new_file_name)
        os.rename(dst_file, new_dst_file_name)

""" render the vagrant file template """

# render jinja2 template with args
def render_template(template_arg, **kwargs):
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




""" for each item in the config array create new vagrantfile , render the
template, vagrant up in subprocess and capture stderror if it exists"""
if __name__ == "__main__":
    config = open_configs()
    runProcess('rm -rf temp')
    i = 0
    load_command = config['command']
    for system in config['systems']:
        # print system
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

    # traverse directory creating VMs
    vms = get_filepaths('temp')
    print vms
    print "RUNNING VM's"
    runProcess('pwd')
    '''
    for vFile in vms:
        runProcess('cd ' + vFile + '; cat Vagrantfile')
    '''
