#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_stati
"""
from fabric.api import local
from datetime import datetime
import os


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
