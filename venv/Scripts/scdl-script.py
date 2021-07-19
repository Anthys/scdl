#!C:\Users\julba\Documents\Github\scdl\venvtest\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'scdl==1.6.12','console_scripts','scdl'
__requires__ = 'scdl==1.6.12'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('scdl==1.6.12', 'console_scripts', 'scdl')()
    )
