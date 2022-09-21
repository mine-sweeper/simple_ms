import os
import sys


def notice(*args):
    frame = sys._getframe().f_back
    filename = frame.f_code.co_filename
    line = frame.f_lineno
    print "[notice]", filename, line, args

def debug(*args):
    frame = sys._getframe().f_back
    filename = frame.f_code.co_filename
    line = frame.f_lineno
    print >> sys.stderr, "[debug]", filename, line, args

