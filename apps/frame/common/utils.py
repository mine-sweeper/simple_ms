import os
import sys


def notice(*args):
    frame = sys._getframe().f_back
    filename = frame.f_code.co_filename
    line = frame.f_lineno
    print("[notice]", filename, 'line', line, ':', *args)

def debug(*args):
    frame = sys._getframe().f_back
    filename = frame.f_code.co_filename
    line = frame.f_lineno
    print("[debug]", filename, 'line', line, ':', *args, file=sys.stderr)

