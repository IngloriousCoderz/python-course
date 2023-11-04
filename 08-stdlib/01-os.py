import os

cwd = os.getcwd()
print(cwd)

os.mkdir('files')
os.chdir('/home/iceonfire')
print(os.getcwd())
os.system('touch myfile.txt')

import shutil

shutil.move('/home/iceonfire/myfile.txt', cwd + '/files')
os.chdir(cwd)
shutil.copyfile('files/myfile.txt', 'files/clone.txt')
shutil.rmtree('files')

# For extra features of shutil @see https://docs.python.org/3/library/shutil.html#module-shutil

from glob import glob

print(glob('*.py')) # ['01-os.py']

import sys

sys.exit(1) # quit the program with an error
sys.exit('An error occurred.') # use a custom message
