#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_stati
"""
from fabric.api import local, run, env, put
from datetime import datetime
import os

env.hosts = ["54.210.96.236", "54.90.1.246"]


def do_pack():
    """Function that generates .tgz file"""

    local("mkdir -p versions")
    t = datetime.now().strftime("%Y%m%d%H%M%S")

    f_path = f"versions/web_static_{t}.tgz"
    result = local(f"tar -cvzf {f_path} web_static")

    size = os.path.getsize(f_path)
    print(f"web_static packed: {f_path} -> {size}")
    if result.failed:
        return None
    return f_path


"""
Fabric script method do_deploy
deploys archive to webservers
"""


def do_deploy(archive_path):
    """Deploy archive to web servers"""

    if os.path.isfile(archive_path) is False:
        return False

    try:
        file_archive = archive_path.split("/")[-1]
        file = file_archive.split(".")[0]
        path = f"/data/web_static/releases/{file}/"
        link = "/data/web_static/current"

        put(archive_path, f"/tmp/{file_archive}")
        run(f"mkdir -p {path}")
        run(f"tar -xzf /tmp/{file_archive} -C {path}")
        run(f"rm -rf /tmp/{file_archive}")
        run(f"mv {path}web_static/* {path}")
        run(f"rm -rf {path}web_static")
        run(f"rm -rf {link}")
        run(f"ln -s {path} {link}")
        print("New version deployed!")

        return True

    except Exception:
        return False


def deploy():
    """Archives and deploys the static files"""

    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False
