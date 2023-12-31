from tools.common_imports import *

#function to update and upgrade debian-based Linux OS
def update_upgrade_debian():
    print("Updating and upgrading debian-based Linux OS")
    print("Updating...")
    time.sleep(2)
    subprocess.call(['sudo', 'apt', 'update', '-y'])
    print("Upgrade...")
    time.sleep(2)
    subprocess.call(['sudo', 'apt', 'full-upgrade', '-y'])
    print("Done")
    print("")

#function to list all outdated applications on debian-based Linux OS and check against cve's and vulnerabilities
def list_outdated_applications_debian():
    print("Listing all outdated applications on debian-based Linux OS")
    print("Listing...")
    time.sleep(2)
    subprocess.call(['sudo', 'apt', 'list', '--upgradable'])
    print("Done")
    print("")
    print("Checking against cve's and vulnerabilities")
    print("Checking...")
    time.sleep(2)
    subprocess.call(['sudo', 'apt', 'list', '--upgradable', '2>/dev/null', '|', 'grep', 'security'])
    print("Done")

#function to install and configure openvas on debian-based Linux OS
def install_security_applications_debian():
    print("Installing openvas for Linux OS")
    print("Installing...")
    time.sleep(2)
    subprocess.call(['sudo', 'apt', 'install', 'openvas', '-y'])
    print("Done")
    print("")
    print("Updating openvas nvt's")
    print("Updating...")
    time.sleep(2)
    subprocess.call(['sudo', 'greenbone-nvt-sync'])
    print("Done")
    print("")
    print("Updating openvas scap data")
    print("Updating...")
    time.sleep(2)
    subprocess.call(['sudo', 'greenbone-scapdata-sync'])
    print("Done")
    print("")
    print("Updating openvas cert data")
    print("Updating...")
    time.sleep(2)
    subprocess.call(['sudo', 'greenbone-certdata-sync'])
    print("Done")
    print("")
    print("Starting openvas")
    print("Starting...")
    time.sleep(2)
    subprocess.call(['sudo', 'openvas-start'])
    print("Done")
    print("")
    print("Creating openvas admin user")
    print("Creating...")
    time.sleep(2)
    subprocess.call(['sudo', 'openvasmd', '--create-user=admin', '--role=Admin'])
    print("Done")
    print("")
    print("Setting openvas admin user password")
    print("Setting...")
    time.sleep(2)
    #variable that will generate a random password for the openvas admin user
    randompassword = subprocess.call(['openssl', 'rand', '-base64', '32'])
    subprocess.call(['sudo', 'openvasmd', '--user=admin', '--new-password=$ramdompassword'])
    #print the $randompassword variable
    print("Your openvas admin user password is: $randompassword")
    print("Done")
    print("")
    print("Starting openvas")
    print("Starting...")
    time.sleep(2)
    subprocess.call(['sudo', 'openvas-start'])
    print("Done")
    print("")

#function that install both nmap and nmap python library on debian-based Linux OS
def install_nmap_debian():
    print("Installing nmap and nmap python library on debian-based Linux OS")
    print("Installing...")
    time.sleep(2)
    subprocess.call(['sudo', 'apt', 'install', 'nmap', '-y'])
    print("Done")
    print("")
    print("Installing nmap python library")
    print("Installing...")
    time.sleep(2)
    subprocess.call(['sudo', 'pip3', 'install', 'python-nmap'])
    print("Done")
    print("")
    print("Checking nmap version")
    print("Checking...")
    time.sleep(2)
    subprocess.call(['nmap', '--version'])
    print("Done")
    print("")
    print("Checking nmap python library version")
    print("Checking...")
    time.sleep(2)
    subprocess.call(['pip3', 'show', 'python-nmap'])
    print("Done")
    print("")

#function to do a vulnerability scan on the same host using python's nmap library and store it in a file named "vulnerability_scan $(date +%Y-%m-%d_%H:%M:%S).txt" on same directory.
def nmap_vulnerability_scan_debian():
    print("Doing vulnerability scan on the same host")
    print("Scanning...")
    time.sleep(2)
    subprocess.call(['sudo', 'nmap', '-sV', '-sC', '-O', '-oN', 'vulnerability_scan $(date +%Y-%m-%d_%H:%M:%S).txt', ' localhost'])
    print("Done")
    print("")
    #lets print the vulnerability scan results file name and location absolute path as we did in the previous lines
    print("Your vulnerability scan results file name is: vulnerability_scan $(date +%Y-%m-%d_%H:%M:%S).txt")
    print("Your vulnerability scan results file location is: $(pwd)")
    print("")
    print("Done")
    print("")

# list_outdated_applications_debian
# install_nmap_debian()
# vulnerability_scan_debian()

    