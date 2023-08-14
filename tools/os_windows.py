from tools.common_imports import *

#lets create a function to update windows OS invoking powershell
def update_upgrade_windows():
    print("Updating and upgrading windows OS")
    print("Updating...")
    time.sleep(2)
    subprocess.call(['powershell', 'Get-WindowsUpdate', '-Install', '-AcceptAll'])
    print("Done")
    print("")