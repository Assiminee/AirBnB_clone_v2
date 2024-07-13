#!/usr/bin/python3


from fabric.api import cd, local, put, run, sudo
from datetime import datetime
from os.path import exists
from fabric.io import env

env.hosts = ['52.3.243.178', '54.197.105.101']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """
        distributes an archive to your web servers
    """
    if not exists(archive_path):
        return False

    archive_file = archive_path.split('/')[1]
    filename = archive_file.split('.')[0]
    destination_folder = f"/data/web_static/releases/{filename}"

    try:
        put(archive_path, '/tmp')
        run(f"mkdir -p {destination_folder}")
        run(f"tar -xvzf /tmp/{archive_file} -C {destination_folder}")
        run(f"rm -rf /tmp/{archive_file} /data/web_static/current")
        run(f"ln -sf {destination_folder} /data/web_static/current")
        return True
    except Exception:
        return False
