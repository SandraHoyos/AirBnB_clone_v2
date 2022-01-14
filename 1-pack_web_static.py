#!/usr/bin/python3
"""
script generates archive from web_static
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    function that creates
    """
    try:
        local("mkdir -p versions")
        date_create = datetime.now().strftime("%Y%m%d%H%M%S")
        directory = "versions/webstatic_{}.tgz".format(date_create)
        zip_ok = local("tar -cvzf {} web_static".format(directory))
        return directory
    except Exception:
        return None
