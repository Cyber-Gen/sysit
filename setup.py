import subprocess
import os
import sys

# Read required packages and modules from requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

# Check if required packages are installed
installed = subprocess.check_output(['pip', 'freeze'])
installed = [pkg.decode().split('==')[0] for pkg in installed.split()]

# Install missing packages
missing = [pkg for pkg in required if pkg.split('==')[0] not in installed]
if missing:
    subprocess.call(['pip', 'install'] + missing)

# Check Python version
with open('requirements.txt') as f:
    for line in f:
        if line.startswith('python=='):
            required_version = line.split('==')[1]
            if not (required_version.startswith('2') and sys.version_info.major == 2) and not (required_version.startswith('3') and sys.version_info.major == 3):
                raise ValueError(f"Python version {required_version} is required, but you are running Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

# Create folder for program installation
if not os.path.exists('sysit'):
    os.makedirs('sysit')

# Clone additional GitHub repository
subprocess.call(['git', 'clone', 'https://github.com/CVEProject/cvelistV5.git', 'sysit/repo'])