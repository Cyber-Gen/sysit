import subprocess
import os
import sys
from pkg_resources import get_distribution, DistributionNotFound


# Check Python version
if sys.version_info < (3, 0):
    print("This program requires Python version 3 or greater.")
    print("\nSetup failed. Please install the required version of Python and try again.")
    sys.exit(1)

# Read required packages and modules from requirements.txt
try:
    with open('requirements.txt') as f:
        required = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("\nError: requirements.txt file not found.")
    print("\nSetup failed.")
    sys.exit(1)

# Check if required packages are installed
installed = []
for pkg in required:
    try:
        get_distribution(pkg.split('==')[0])
        installed.append(pkg)
    except DistributionNotFound:
        print("\nDistribution Not Found")
        print("\nSetup failed.")
        sys.exit(1)

# Install missing packages
missing = [pkg for pkg in required if pkg not in installed]
if missing:
    print(f"\nInstalling missing packages: {', '.join(missing)}")
    try:
        subprocess.call(['pip', 'install'] + missing)
    except subprocess.CalledProcessError:
        print("\nError: failed to install missing packages.")
        print("\nSetup failed.")
        sys.exit(1)


# Create folder for program installation
if not os.path.exists('sysit'):
    try:
        os.makedirs('sysit')
    except OSError:
        print("\nError: failed to create folder for program installation.")
        print("\nSetup failed.")
        sys.exit(1)

if not os.path.exists('sysit/repos'):
    try:
        os.makedirs('sysit/repos')
    except OSError:
        print("\nError: failed to create folder for program installation.")
        print("\nSetup failed.")
        sys.exit(1)

if not os.path.exists('sysit/reports'):
    try:
        os.makedirs('sysit/reports')
    except OSError:
        print("\nError: failed to create folder for program installation.")
        print("\nSetup failed.")
        sys.exit(1)

if not os.path.exists('sysit/repos/cvelistV5'):
    try:
        subprocess.call(['git', 'clone', 'https://github.com/CVEProject/cvelistV5.git', 'sysit/repos/cvelistV5'])
    except OSError:
        print("\nError: failed to create folder for program installation.")
        print("\nSetup failed.")
        sys.exit(1)

print("\nEverything looks good.\nSetup complete!")

