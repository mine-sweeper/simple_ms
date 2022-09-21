import os
import sys


class BaseParallelProcessor(object):
    def __init__(self, context):
        self._context = context
        self.type = 'parallel'

    def split(self):
        return True

    def merge(self):
        return True

