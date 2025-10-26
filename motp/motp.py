"""
mOTP lib

motp code generator
https://motp.sourceforge.net/
https://motp.n4n5.dev/
https://github.com/Its-Just-Nans/motp
"""

from time import time
from hashlib import md5
from os.path import isfile, expanduser
from argparse import ArgumentParser

# pylint: disable-next=redefined-builtin
from sys import stderr, exit


def get_var(filename):
    """get variable from file"""
    if not isfile(filename):
        print(
            f"'{filename}' is not found",
            file=stderr,
        )
        return None
    with open(filename, "r", encoding="utf-8") as f:
        txt = f.read().strip()
    if txt == "":
        print(
            f"'{filename}' is empty",
            file=stderr,
        )
        return None
    return txt


def motp(secret: str, pin: str):
    """generates mOTP"""
    epoch_time = int(time())
    counter = epoch_time // 10
    string_to_hash = f"{counter}{secret}{pin}"
    md5_hash = md5(string_to_hash.encode()).hexdigest()[:6]
    return md5_hash


def main():
    """main motp"""
    parser = ArgumentParser(description="mOTP cli")

    parser.add_argument("-s", type=str, help="secret")
    parser.add_argument("-p", type=str, help="pin")

    parser.add_argument("--file-secret", type=str, help="Path to secret file")
    parser.add_argument("--file-pin", type=str, help="Path to PIN file")

    args = parser.parse_args()
    secret = None
    if args.s:
        if args.s == "-":
            secret = input("Enter secret:")
        else:
            secret = args.s
    elif args.file_secret:
        secret = get_var(args.file_secret)
    else:
        secret = get_var(expanduser("~/.motp-hex"))
    if secret is None:
        print(
            "Error: no secret",
            file=stderr,
        )
        exit(1)
    pin = None
    if args.p:
        if args.p == "-":
            secret = input("Enter pin:")
        else:
            pin = args.p
    elif args.file_pin:
        pin = get_var(args.file_pin)
    else:
        pin = get_var(expanduser("~/.motp-pin"))
    if pin is None:
        print(
            "Error: no pin",
            file=stderr,
        )
        exit(1)
    code = motp(secret, pin)
    print(code)


if __name__ == "__main__":
    main()
