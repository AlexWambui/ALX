#!/usr/bin/python3
"""This compresses a web static package
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['18.235.249.190', '52.91.151.166']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
        """Deploy web files to both servers
        """
        try:
                if not (path.exists(archive_path)):
                        return False

                # upload the archive
                put(archive_path, '/tmp/')

                # create target dir
                timestamp = archive_path[-18:-4]
                run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

                # uncompress the archive and delete .tgz
                run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                    .format(timestamp, timestamp))

                # remove archive
                run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

                # move contents into host web_static
                run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

                # remove exisiting web_static dir
                run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
                    .format(timestamp))

                # delete the existing sym link
                run('sudo rm -rf /data/web_static/current')

                # re-create a symbolic link
                run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
        except:
                return False

        # return True on success
        return True
