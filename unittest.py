import unittest2 as unittest
import virtual_machine
import vcluster
import yaml
import json
import sys
import os


class vclusterTests(unittest.TestCase):

    def test_yaml_config(self):
        config = vcluster.open_config('settings.yaml')
        self.assertEqual(config['command'], 'python unittest.py')

    def test_json_config(self):
        config = vcluster.open_config('sample.json')
        self.assertEqual(config['command'], 'python unittest.py')

    def test_config_ftype(self):
        with open('settings.csv', 'w') as f:
            f.write("hello there, I'm not a config file")
        config = vcluster.open_config('settings.csv')
        self.assertFalse(config)

    def check_vagrantfiles(self):
        """
        make a temp_cluster folder, scrape it for clarity
        """
        config = vcluster.open_config('settings.yaml')
        vm_list = vcluster.generate_machines()
        if false in [vm == type(vm) for vm in vm_list]:
            raise ValueError("item in list wasn't vm type?")

    def test_render_clusters(self):
        """
        create vagrant files for a vcluster,
        make sure templates render correctly
        """
        return  # TODO double check this!

    def double_check_folder_kill(self):
        """
        make a temp_cluster folder, remove it
        """
        config = vcluster.open_config('settings.yaml')
        vm_list = vcluster.generate_machines()
        self.assertEqual(True, clear_vms())






if __name__ == '__main__':
    unittest.main()
