#Below script automates the installation of required dependencies listed in Requirements.txt
#inspired by StackOverflow post :
#https://stackoverflow.com/questions/12332975/how-can-i-install-a-python-module-with-pip-programmatically-from-my-code


import pkg_resources
import sys
import subprocess

#automating the list of requirements installation
f = open("Requirements.txt", "r")
requirements = f.readlines()
f.close()

#debug
#print(requirements)

dependency = {}

#filtering requirements from other text
for requirement in requirements:
    if requirement[:1].isalpha(): #check if it is a dependency or to be discarded
        requirement = requirement.split()
        #allows only if the first character is a letter and the second is a number (to avoid comments or malformed lines)
        if requirement[0][:1].isalpha() and requirement[1][:1].isnumeric():
            dependency[requirement[0]] = requirement[1]


#checking if dependency installed and at right version
for d in dependency:
    name = d
    version = dependency[d]

    try:
        pkg = pkg_resources.get_distribution(name)

        # version mismatch
        if pkg.version != version:
            print(f"Version mismatch for {name}: installed {pkg.version}, required {version}. Installing correct version...")
            #installing the correct version according to the best methods described in StackOverflow post : https://stackoverflow.com/questions/12332975/how-can-i-install-a-python-module-with-pip-programmatically-from-my-code
            subprocess.check_call([sys.executable, "-","pip", "install", "--upgrade", f"{name}=={version}"])

        # correct version already installed
        else:
            print(f"{name} is already installed at the required version {version}.")

    # package not found
    except pkg_resources.DistributionNotFound:
        print(f"{name} not found. Installing version {version}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", f"{name}=={version}"])

