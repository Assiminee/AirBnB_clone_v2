#!/usr/bin/python3


from fabric.api import local, env
from datetime import datetime

env.hosts = ['52.3.243.178', '54.197.105.101']
env.user = 'ubuntu'


def do_pack():
    """
        Packs the contents of the web_static folder
        into an archive where the name is in the format
        web_static_<year><month><day><hour><minute><second>.tgz
    """
    local("mkdir -p versions")
    dttime = datetime.now().strftime('%Y%m%d%H%M%S')
    archive: str = f"versions/web_static_{dttime}.tgz"
    res = local(
        f"tar -cvzf {archive} web_static",
        capture=True
    )
    if res:
        return archive
    return None
