import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-jupyter", help="Installs Jupyter Notebook dependencies.", action="store_true")
args = parser.parse_args()

if(args.jupyter):
    cmd = "conda env create -f environment_with_jupyter.yml"
else:
    cmd = "conda env create -f environment_without_jupyter.yml"

try:    
    os.system(cmd)
except:
    print("Could not install the specidied environment!")
