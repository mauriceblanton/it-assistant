# imports:
import sys
from cx_Freeze import setup, Executable

# configure_platforms:
base = None
if sys.platform == 'win32' : base = 'Win32GUI'
5
# includes:
setup(name = 'IT Assistant',
      version = '1.2',
      description = 'Shows PC name, IP address and confirms WAN connectivity.',
      categories = 'PC troubleshooting, network connectivity, help desk',
      comments = 'Made with Python...',
      author = 'Maurice G. Blanton Jr.',
      executables = [Executable('it-assistant.py', base = base)])
