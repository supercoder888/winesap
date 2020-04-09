##Usage
Command:

```vol.py --plugins=AutoRuns/plugin --profile=Win7SP1x64 -f dump.vmem autoruns```

Help:

```
Search for all Autostart Extensibility Points (AESPs)

Options:
    --match: only shows suspicious entries
```

##Help scripts

Under ```lab``` folder there are some scripts to simulate an infection on a Windows system. You can run them one by one or use ```runall.py``` to run them all (needs a privileged command line).

Anyway, there is available an [infected memory dump](https://drive.google.com/file/d/1f6E3mCQMu86UDk3j2PkHSbF63YJOctND/) with all scripts executed.

###Dependencies

```pip install pywin32``` in order to work with Windows registers.
