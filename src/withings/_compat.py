# -*- coding: utf-8 -*-

import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY3:
    import configparser

    input = input

elif PY2:
    import ConfigParser as configparser

    input = raw_input

else:
    raise RuntimeError('Unsupported python version.')
