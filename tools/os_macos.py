from tools.common_imports import *

#function to update and upgrade macos
def update_upgrade_macos():
    print("Updating and upgrading macos")
    print("Updating...")
    time.sleep(2)
    subprocess.call(['sudo', 'softwareupdate', '-i', '-a'])
    #if softwareupdate is successful, it will return 0. if not, it will return 1.
    if subprocess.call(['sudo', 'softwareupdate', '-i', '-a']) == 0:
        print("\n OS update successfully completed.")
        time.sleep(3)
    else:
        print("\n OS update failed.")
        sys.exit(1)

#function to install homebrew on macos
def install_homebrew_macos():
    print("Installing homebrew on macos")
    print("Installing...")
    time.sleep(2)
    subprocess.call(['/bin/bash', '-c', '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)'])
    print("Done")
    print("")

#function to update all applications on macos
def update_upgrade_applications_macos():
    print("Updating and upgrading applications on macos")
    print("Updating...")
    time.sleep(2)
    subprocess.call(['brew', 'update'])
    print("Upgrade...")
    time.sleep(2)
    subprocess.call(['brew', 'upgrade'])
    print("Done")
    print("")