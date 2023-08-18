from tools.common_imports import *

#function to update windows OS invoking powershell
def update_upgrade_windows():
    print("Updating and upgrading windows OS")
    print("Updating...")
    time.sleep(2)
    subprocess.call(['powershell', 'Get-WindowsUpdate', '-Install', '-AcceptAll'])
    print("Done")
    print("")

#function to install latest chocolatey version on windows OS
def install_chocolatey_windows():
    print("Installing chocolatey for windows OS")
    print("Installing...")
    time.sleep(2)
    subprocess.call(['powershell', 'Set-ExecutionPolicy', 'Bypass', '-Scope', 'Process', '-Force;[System.Net.ServicePointManager]::SecurityProtocol', '= [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))'])
    print("Done")
    print("")
    print("Checking chocolatey version")
    print("Checking...")
    time.sleep(2)
    subprocess.call(['powershell', 'choco', '--version'])