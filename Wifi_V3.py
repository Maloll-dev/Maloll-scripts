import os
from pystyle import Colors, Colorate
import re
import subprocess
import time

# Display the main menu
print(Colorate.Vertical(Colors.red_to_purple, """
██╗    ██╗██╗███████╗██╗    ███╗   ███╗██╗   ██╗██╗  ████████╗██╗    ████████╗ ██████╗  ██████╗ ██╗     
██║    ██║██║██╔════╝██║    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║ █╗ ██║██║█████╗  ██║    ██╔████╔██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     
██║███╗██║██║██╔══╝  ██║    ██║╚██╔╝██║██║   ██║██║     ██║   ██║       ██║   ██║   ██║██║   ██║██║     
╚███╔███╔╝██║██║     ██║    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                                                        
""", 2))

print(Colorate.Diagonal(Colors.white_to_red, """ 
[1] Wifi Password (take the passwords of the wifi you have already connected to)
[2] Wifi List (list of the wifi you have already connected to)
[3] Wlan Info (get all the information about your wifi)

""", 1))

# Prompt the user for selection
select = int(input("Selection: "))

# Function to display wifi profiles and get passwords
def get_wifi_passwords():
    os.system('cls')
    time.sleep(0.40)
    print(Colorate.Vertical(Colors.white_to_green, """ 
██╗    ██╗██╗███████╗██╗    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
██║    ██║██║██╔════╝██║    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██║ █╗ ██║██║█████╗  ██║    ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██║███╗██║██║██╔══╝  ██║    ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
╚███╔███╔╝██║██║     ██║    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝    ╚═╝     ╚═╝  ╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                                                                               
    """, 2))
    time.sleep(0.35)
    
    netsh_cmd = 'netsh wlan show profiles'
    netsh_output = subprocess.check_output(netsh_cmd, shell=True, encoding='utf-8')
    
    # Extract wifi profile names
    pattern = r"    Profil Tous les utilisateurs\s*:\s*(.*)"
    profile_names = re.findall(pattern, netsh_output)
    
    if profile_names:
        for profile_name in profile_names:
            profile_name = profile_name.strip()
            netsh_cmd = f'netsh wlan show profile name="{profile_name}" key=clear'
            netsh_output = subprocess.check_output(netsh_cmd, shell=True, encoding='utf-8')
            pattern = r'Contenu de la clé\s+:\s+(.+)'
            match = re.search(pattern, netsh_output)
            if match:
                key_content = match.group(1)
                print(Colorate.Horizontal(Colors.white_to_green, f"{profile_name} : {key_content}"))
            else:
                print(Colorate.Horizontal(Colors.white_to_green, f"{profile_name} : Password not found"))
    else:
        print(Colorate.Horizontal(Colors.white_to_green, "No profile found", 2))
    
    print()
    print(Colorate.Horizontal(Colors.red_to_yellow, "press enter to exit", -1))
    input()

# Function to display list of wifi profiles
def list_wifi_profiles():
    os.system('cls')
    netsh_cmd = 'netsh wlan show profiles'
    netsh_output = subprocess.check_output(netsh_cmd, shell=True, encoding='utf-8')
    
    # Extract wifi profile names
    pattern = r"    Profil Tous les utilisateurs\s*:\s*(.*)"
    profile_names = re.findall(pattern, netsh_output)
    
    if profile_names:
        for profile_name in profile_names:
            print(Colorate.Horizontal(Colors.white_to_green, profile_name.strip(), 2))
    else:
        print(Colorate.Horizontal(Colors.white_to_green, "No profile found", 2))
    print()
    print(Colorate.Horizontal(Colors.red_to_yellow, "press enter to exit", -1))
    input()
# Function to display WLAN information
def show_wlan_info():
    os.system('cls')
    os.system('cmd /c "netsh wlan show interfaces"')
    print()
    print(Colorate.Horizontal(Colors.red_to_yellow, "press enter to exit", -1))
    input()

# Execute the selected function
if select == 1:
    get_wifi_passwords()
elif select == 2:
    list_wifi_profiles()
elif select == 3:
    show_wlan_info()
else:
    print("Invalid selection")
