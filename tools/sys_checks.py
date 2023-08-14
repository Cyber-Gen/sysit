from tools.common_imports import *


os_type = None

def check_os():
  
  if platform.system() == "Windows":
    print("Windows OS detected")
    #let's make sure the if the OS is windows, the os_type variable is set to "windows" and can be used in other functions and modules.
    os_type = "windows"
    import tools.os_windows
    
  elif platform.system() == "Linux":
    print("Linux OS detected")
    os_type = "linux"
    import tools.os_linux
    
  elif platform.system() == "Darwin": 
    print("MacOS detected")
    os_type = "macos"
    import tools.os_macos
  else:
    print("OS is not supported") 
    sys.exit(1)
  
  return os_type

#lets define function that checks network status, public IP, system's dns resolver.
def check_ping():
    
    # print("Testing network status")
    # print("Testing...")
    time.sleep(2)
    #if ping is successful, it will return 0. if not, it will return 1.
    if subprocess.call(['ping', '-c', '3', 'google.com']) == 0:
        print("\nPing test is successful.")
        time.sleep(3)
    else:
        print("\nPing test failed.")
        sys.exit(1)
    print("")


def check_ip():
    
    # print("Checking public IP address")
    # print("Checking...")
    time.sleep(2)
    #if curl is successful, it will return 0. if not, it will return 1.
    if subprocess.call(['curl', 'ifconfig.me']) == 0:
        print("\nPublic IP test is successful.")
        time.sleep(3)
    else:
        print("\nPublic IP test failed.")
        sys.exit(1)
    print("")

def check_dns_config():
    
    # print("Checking system's DNS resolver configuration")
    # print("Checking...")
    time.sleep(2)
    #test this only if the OS is linux or macos
    if os_type == "linux" or "macos":
        if subprocess.call(['cat', '/etc/resolv.conf']) == 0:
            print("\nDNS resolver test is successful.")
            time.sleep(3)
        else:
            print("\nDNS resolver test failed.")
            sys.exit(1)
    elif os_type == "Windows":
        print("\nsystem DNS resolver test is not supported on Windows.")
        print("")
    else:
        print("\nOS is not supported.")
        sys.exit(1)

def check_dns():

    # print("Testing DNS resolver")
    # print("Testing...")
    time.sleep(2)
    #if nslookup is successful, it will return 0. if not, it will return 1.
    if subprocess.call(['nslookup', 'google.com']) == 0:
        print("\nDNS resolver test is successful.")
        time.sleep(3)
    else:
        print("\nDNS resolver test failed.")
        sys.exit(1)