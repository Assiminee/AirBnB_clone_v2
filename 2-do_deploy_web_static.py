#!/usr/bin/python3


from fabric.api import sudo, put, run, env
from os.path import exists

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
        run(f"sudo mkdir -p {destination_folder}")
        run(f"sudo tar -xzf /tmp/{archive_file} -C {destination_folder}")
        run(f"sudo mv {destination_folder}/web_static/* {destination_folder}")
        run(f"sudo rm -rf /tmp/{archive_file}")
        run(f"sudo rm -rf /data/web_static/current")
        run(f"sudo rm -rf {destination_folder}/web_static")
        run(f"sudo ln -sf {destination_folder}/ /data/web_static/current")
        sudo("service nginx restart")
        return True
    except Exception:
        return False
