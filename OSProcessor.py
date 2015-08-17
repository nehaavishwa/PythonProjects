__author__ = 'nehaavishwa'


import os
import pwd
print(os.getlogin())
print(os.getuid())
print(pwd.getpwuid(os.getuid()))