#!/bin/env python3
"""motp code generator
https://motp.sourceforge.net/
https://motp.n4n5.dev/
https://github.com/Its-Just-Nans/motp
"""

import os
import time
import hashlib
import sys


def get_var(filename):
    """get variable from file"""
    if not os.path.isfile(filename):
        print(
            f"{filename} is not found - the MOTP code will be incorrect",
            file=sys.stderr,
        )
    with open(filename, "r", encoding="utf-8") as f:
        txt = f.read().strip()
    return txt


def main():
    """main function"""
    secret = get_var(os.path.expanduser("~/motp-hex"))
    pin = get_var(os.path.expanduser("~/motp-pin"))
    epoch_time = int(time.time())
    counter = epoch_time // 10
    string_to_hash = f"{counter}{secret}{pin}"
    md5_hash = hashlib.md5(string_to_hash.encode()).hexdigest()[:6]
    print(md5_hash)


if __name__ == "__main__":
    main()
