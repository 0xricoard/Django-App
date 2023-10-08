import subprocess
import sys
import random
import string
import sys

def generate_random_string():
  characters = string.ascii_letters + string.digits + string.punctuation
  random_string = ''.join(random.choice(characters) for _ in range(50))
  return random_string

def running_command(command):
  subprocess.call(command)

def installing_all_libraries():
  running_command(["pip", "install", "-r", "installed_packages.txt"])

def installing_specific_library(library_name):
  running_command(["pip", "install", library_name])

def migrate():
  running_command(["py", "manage.py", "migrate"])

def running_server():
  running_command(["py", "manage.py", "runserver"])

def running_installing():
  with open('installed_packages.txt', 'r') as file:
    required_libraries = [line.strip() for line in file]

  installed_libraries = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode ('utf-8').split('\n')
  installed_set = set(installed_libraries)
  not_installed = [lib for lib in required_libraries if lib not in installed_set]

  if len(not_installed) < len(required_libraries):
    print("Installing libraries... Please Wait")
    installing_all_libraries()
    migrate()
  else:
    print("Installing libraries... Please Wait")
    for lib in not_installed:
      installing_specific_library(lib)
    migrate()

if 'key' in sys.argv:
  print("\nYour key: '{key}'\n".format(key=generate_random_string()))
elif '-s' in sys.argv:
  running_command(["py", "manage.py", "runserver"])
elif '-t' in sys.argv and '--r' in sys.argv:
  running_command(["py", "manage.py", "tailwind", "start"])
elif '-t' in sys.argv and '--i' in sys.argv:
  print('Installing tailwind... Please Wait')
  running_command(["py", "manage.py", "tailwind", "install"])
else:
  running_installing()