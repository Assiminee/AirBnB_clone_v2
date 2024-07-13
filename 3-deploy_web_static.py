#!/usr/bin/python3


from fabric.api import local, put, run, env
from datetime import datetime
from os.path import exists


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
    if not exists(archive_path):
        return False

    env.hosts = ['52.3.243.178', '54.197.105.101']
    archive_file = archive_path.split('/')[1]
    filename = archive_file.split('.')[0]
    destination_folder = f"/data/web_static/releases/{filename}"

    try:
        put(archive_path, '/tmp')
        run(f"mkdir -p {destination_folder}")
        run(f"tar -xzf /tmp/{archive_file} -C {destination_folder}")
        run(f"mv {destination_folder}/web_static/* {destination_folder}")
        run(f"rm -rf /tmp/{archive_file}")
        run(f"rm -rf /data/web_static/current")
        run(f"rm -rf {destination_folder}/web_static")
        run(f"ln -sf {destination_folder}/ /data/web_static/current")
        return True
    except Exception:
        return False


def deploy():
    """
        executes do_pack() and do_deploy()
        to deploy web_static to the servers
    """
    archive_path = do_pack()

    if not archive_path:
        return False

    return do_deploy(archive_path)
