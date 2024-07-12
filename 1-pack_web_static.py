#!/usr/bin/python3

from fabric.api import local


def do_pack():
    """
        Packs the contents of the web_static folder
        into an archive where the name is in the format
        web_static_<year><month><day><hour><minute><second>.tgz
    """
    local("[ -d versions ] || mkdir versions")
    datetime = local(
        """
        timedatectl | awk 'NR==1 {
        gsub(\"-\", \"\");
        gsub(\":\", \"\");
        print $4 $5}'
        """
    )
    res = local(
        f"tar -cvzf versions/web_static_${datetime}.tgz web_static",
        capture=True
    )
    if res:
        return res
    return None
