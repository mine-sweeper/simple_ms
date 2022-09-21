import os
import sys


class BaseStageProcessor(object):
    def __init__(self):
        pass

    def split(self, context, subcontext):
        return True

    def process(self, subcontext):
        return True

    def merge(self, subcontext, context):
        return True

