import os
import sys
from .request import Request


class Context(dict):
    def __init__(self):
        super(Context, self).__init__()
        self.request = Request()
        self.response = None
        self.stage = {}
        self.conf = {}
        self.handler_factory = {}
        self.data_service = None

    def kage_bunshin(self):
        ret = Context()
        ret.request = self.request
        ret.handler_factory = self.handler_factory
        ret.conf = self.conf
        ret.stage = dict()
        return ret

