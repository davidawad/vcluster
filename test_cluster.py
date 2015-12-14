##
# vcluster unit tests
# @author David Awad
#

import unittest2 as unittest
import virtual_machine
import vcluster
import yaml
import json
import sys
import os


class vclusterTests(unittest.TestCase):

    def setUp(self):
        self.config = vcluster.open_config('settings.yaml')

    def test_yaml_config(self):
        config = vcluster.open_config('settings.yaml')
        self.assertEquals(config['command'], 'python unittest.py')
        self.assertTrue(config['command'])

    def test_json_config(self):
        # FIXME JSON support is actually totally untested.
        config = vcluster.open_config('sample.json')
        # self.assertEquals(config['command'], 'python unittest.py')
        # self.assertTrue(config['command'])

    def test_config_ftype(self):
        with open('settings.csv', 'w') as f:
            f.write("hello there, I'm not a config file")
        config = vcluster.open_config('settings.csv')
        os.remove('settings.csv')
        self.assertFalse(config)

    def test_check_vagrantfiles(self):
        """
        make a temp_cluster folder, scrape it for clarity
        """
        vm_list = vcluster.generate_machines(self.config)
        for item in vm_list:
            self.assertIsInstance(item, virtual_machine.vm)

    def test_render_clusters(self):
        """
        create vagrant files for a vcluster,
        make sure templates render correctly
        """
        return  # TODO double check this!

    def test_clear_vm(self):
        """
        make a temp_cluster folder, remove it
        """
        vm_list = vcluster.generate_machines(self.config)
        self.assertTrue(vcluster.clear_vms())

    def tearDown(self):
        vcluster.clear_vms()
        try:
            os.remove('settings.csv')
        except OSError:
            pass


if __name__ == '__main__':
    unittest.main()
