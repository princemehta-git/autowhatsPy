import os
import platform

osname = platform.system()
username = os.getenv('username')

# profiles_path = 'C:\\Users\\%s\\AppData\\roaming\Opera software\\Opera Stable\\whatsprofile' % username
if "window" in osname.lower():
    profiles_path = 'C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\User Data\\' % username
elif "darwin" in osname.lower():
    profiles_path = 'Users/%s/Library/Application Support/Google/Chrome/' % username

elif "linux" in osname.lower():
    profiles_path = '/home/%s/.config/google-chrome/' % username


# profiles_path = "C:\\Users\\%s\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\whats_firefox" % username
# for chrome
# Windows 7, 8.1, and 10: C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default
# Mac OS X El Capitan: Users/<username>/Library/Application Support/Google/Chrome/Default
# Linux: /home/<username>/.config/google-chrome/default

# for opera
# 'C:\\Users\\<username>\\AppData\\roaming\Opera software\\Opera Stable'


# for firefox
# C:\Users\<username>\AppData\Roaming\Mozilla\Firefox\Profiles\

setting = {'profiles' : []
           }