import subprocess
import sys

def installing_all_libraries():
  subprocess.call(["pip", "install", "-r", "installed_packages.txt"])

def installing_specific_library(library_name):
  subprocess.call(["pip", "install", library_name])

def migrate():
  subprocess.call(["py", "manage.py", "migrate"])

def running_server():
  subprocess.call(["py", "manage.py", "runserver"])

with open('installed_packages.txt', 'r') as file:
  required_libraries = [line.strip() for line in file]

installed_libraries = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode('utf-8').split('\n')
installed_set = set(installed_libraries)
not_installed = [lib for lib in required_libraries if lib not in installed_set]

if len(not_installed) < len(required_libraries):
  installing_all_libraries()
  migrate()
else:
  for lib in not_installed:
    installing_specific_library(lib)
  migrate()