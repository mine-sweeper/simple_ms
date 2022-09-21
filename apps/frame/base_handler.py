import os
import sys
from copy import copy


class BaseHandler(object):
    factory = {}
    def __init__(self, conf, data):
        self._conf = conf
        self._data = data
        self._result = {}
        pass

    def init(self, params):
        return True

    def run(self, local_feat, target):
        return True

    def get_result(self):
        return self._result

    def kage_bunshin(self):
        ret = copy(self)
        ret._result = {}
        return ret

