class HighLoadAverage(Exception):
    pass

import os
import sys

import argparse

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument(
    "--la",
    required=True,
    help="Set load average rate",
)
import time
args = parser.parse_args()
la = os.getloadavg()[0]
if la > float(args.la):
    print("stop: high loadaverage!! > {}".format(la))
    print(os.getloadavg())
    print("rebooting...")
    time.sleep(10)
    import subprocess
    subprocess.run("reboot",shell=True)
else:
    print("ok: loadaverage = {}".format(la))
