import os
import time
import typing

NS_TO_HOUR = 3600000000000

def read_from_cache(update: typing.Callable[[str], str],
                    fname: str,
                    delay: int = 1):
    try:
        stats = os.stat(fname)
    except FileNotFoundError:
        return update(fname)
    now = time.time_ns()
    if now > (stats.st_mtime_ns + (NS_TO_HOUR * delay)):
        return update(fname)
    file_handle = open(fname, "r")
    content = file_handle.read()
    file_handle.close()
    return content
