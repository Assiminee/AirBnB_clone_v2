#!/usr/bin/python3

from fabric.api import cd, local

def do_pack() :
    with cd("/data/web_static"):
        local("[ -d versions ] || mkdir versions")
        datetime = local(
            """
            timedatectl | awk 'NR==1 {
            gsub(\"-\", \"\");
            gsub(\":\", \"\");
            print $4 $5}'
            """
        )
        res = local(f"tar -cvzf versions/web_static_${datetime}.tgz ./*")
        if res:
            return res
        return None
