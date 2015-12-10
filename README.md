# vcluster [![Code Climate](https://codeclimate.com/github/DavidAwad/vcluster/badges/gpa.svg)](https://codeclimate.com/github/DavidAwad/vcluster)

a CLI for generating Vagrant files and running cross platform clustered unit tests from the command line.

You need to use something like Puppet as a provisioning service in order to make sure when you boot your other virtual machines that they are configured properly.

You can of course edit the `Vagrantfile` any way you see fit in order to make provisioning happen correctly. I've included a basic sample.  

## Requirements
- VirtualBox
- Vagrant
- Puppet
- Python 2.7+

## How it works
So the way this app works is you can open `settings.yaml` in order to create a list of all of the vagrant images you want to build for.

Then you specify what shell command you want to run on the VM.

You should have a list that looks something like this.

```yaml
systems:
      - "hashicorp/precise32"
      - "ubuntu/trusty64"
      - "puphpet/centos65-x64"


command: "./unittest.sh"
```

Then when you run `python vcluster.py`, you should be able to watch the tests run on the different VMs, if anything is logged to standard error the output will appear in red.


## Built at PennApps XII

![](http://2014s.pennapps.com/build/images/logo/dark1.png)

![](https://mlh.io/brand-assets/logo-grayscale/mlh-logo-grayscale-small.png)

## Plugins vcluster uses
[vagrant-digitalocean](https://github.com/smdahlen/vagrant-digitalocean)

[vagrant linode](https://github.com/displague/vagrant-linode)
