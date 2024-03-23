#!/usr/bin/python3
"""
Fabric script method do_deploy
deploys archive to webservers
"""
from fabric.api import env, put, run, sudo
import os.path

env.hosts = ["54.210.96.236", "54.90.1.246"]


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
