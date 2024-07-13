#!/usr/bin/python3

from fabric.api import cd, env, lcd, local, run, sudo

env.hosts = ['52.3.243.178', '54.197.105.101']
env.user = 'ubuntu'


def do_clean(number=0):
    """
         deletes out-of-date archives
         number: the number of the archives,
         including the most recent, to keep
    """
    number = int(number)
    start = number if number > 1 else 1

    with lcd("versions"):
        local(f"ls -t | tail -n +{start + 1} | xargs rm -rf")

    with cd("/data/web_static/releases/"):
        run(f"ls -t | tail -n +{start + 1} | xargs sudo rm -rf")
