#!/usr/bin/python3

from fabric.api import local
from datetime import datetime


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
