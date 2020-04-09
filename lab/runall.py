import os
import sys
import glob
import ctypes
import subprocess

files = [x for x in glob.glob('*.py') if x not in ['winutils.py', os.path.basename(__file__)]]

for f in sorted(files):
    print('Running {0}...'.format(f))
    subprocess.call([sys.executable, f])
