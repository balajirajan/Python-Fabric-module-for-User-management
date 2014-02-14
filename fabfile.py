#!/usr/bin/python

from fabric.api import *

from fabric.network import ssh_config

from os import system

env.roledefs = {
    'linux-servers': ['192.168.0.11'],
}

#env.hosts = ['192.168.0.1']
env.user = 'username'
env.password = 'password'

def new_admin(host=''):
     env.hosts='%s' % host
     run('sudo groupadd admin')
     sudo('echo "%admin ALL=(ALL) ALL" >> /etc/sudoers')

def new_user(user='',host=''):    
     env.hosts='%s' % host
     sudo('adduser %s' % user)
     sudo('usermod  -a -G admin %s' % user)
     sudo('echo "%s:password" | chpasswd' % user)

