#!/usr/bin/python3


from fabric.api import cd, local, put, run, sudo
from datetime import datetime
from os.path import isfile
from fabric.io import env


def do_pack():
    """
        Packs the contents of the web_static folder
        into an archive where the name is in the format
        web_static_<year><month><day><hour><minute><second>.tgz
    """
    local("mkdir -p versions")
    dttime = datetime.now().strftime('%Y%m%d%H%M%S')
    res = local(
        f"tar -cvzf versions/web_static_{dttime}.tgz web_static",
        capture=True
    )
    if res:
        return res
    return None

def do_deploy(archive_path):
    """
        distributes an archive to your web servers
    """
    if not isfile(archive_path):
        return False

    env.hosts = ['52.3.243.178', '54.197.105.101']

    archive_file = archive_path.split('/')[1]
    filename = archive_file.split('.')[0]
    destination_folder = f"/data/web_static/releases/{filename}"

    try:
        put(archive_path, '/tmp')
        sudo(f"mkdir -p {destination_folder}")
        sudo(f"tar -xvzf /tmp/{archive_file} -C {destination_folder}")
        sudo(f"rm -rf /tmp/{archive_file} /data/web_static/current")
        sudo(f"ln -sf {destination_folder} /data/web_static/current")
        return True
    except Exception:
        return False
