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
    try:
        number = int(number)
    except:
        return False

    start = number if number > 1 else 1

    with lcd("versions"):
        local_list = local("ls -t", capture=True)
        local_files = local_list.split()

        for i in range(start, len(local_files)):
            local(f"rm {local_files[i]}")

    with cd("/data/web_static/releases/"):
        remote_list = run("ls -t")
        remote_files = remote_list.split()

        for i in range(start, len(remote_files)):
            if not remote_files[i].startswith("web_static_"):
                continue
            sudo(f"rm {remote_files[i]}")
