#!/usr/bin/env python

# This script is written to simply the updating of torsion drive examples
# It will walk though all subfolders of current folder, find "run_command" file and run the command in it.
# Existing "opt_tmp/" folder will be deleted first before running.
# Then after the job finish, it will compress the "opt_tmp/" folder into "opt_tmp.tar.gz"

import os
import shutil
import subprocess

# walk though the subfolders and find "run_command"
leaf_subfolders = []
for root, dirs, files in os.walk("."):
    if 'run_command' in files:
        leaf_subfolders.append(root)
leaf_subfolders.sort()
n = len(leaf_subfolders)
print(f"Found {n} example folders with run_command")

# go though the list and run examples one by one
curr_path = os.getcwd()
for i, folder in enumerate(leaf_subfolders):
    print(f"{i:4d}/{n:<4d} {folder}")
    os.chdir(folder)
    # delete opt_tmp/ folder if exist
    if os.path.isdir('opt_tmp'):
        shutil.rmtree('opt_tmp')
    # rerun the example
    with open('scan.log', 'w') as logfile:
        with open('worker.log', 'w') as errfile:
            subprocess.run('bash run_command', shell=True, stdout=logfile, stderr=errfile)
    # compress the new opt_tmp folder
    if os.path.isfile('opt_tmp.tar.gz'):
        os.remove('opt_tmp.tar.gz')
    if os.path.isdir('opt_tmp'):
        subprocess.run('tar zcf opt_tmp.tar.gz opt_tmp/', shell=True, check=True)
    os.chdir(curr_path)

