
#Below code inspired by unknown stackoverflow user at : https://stackoverflow.com/questions/1051254/check-if-python-package-is-installed

import importlib.util
import sys

#automating the list of requirements installation
f = open("Requirements.txt", "r")
requirements = f.readlines()
f.close()

#debug
#print(requirements)

dependency = {}

#filtering requirements from other text
for requirement in requirements:
    if requirement[:1].isalpha(): #check if it is a dependency
        requirement = requirement.split()
        dependency[requirement[0]] = requirement[1]

#checking if dependency installed and at right version
for d in dependency:
    name = d
    version = dependency[d]
    print(name, version)

    if name in sys.modules:
        print("Module '{}' already exists".format(name))
    else:
        print("not installed")
