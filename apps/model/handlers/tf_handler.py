import os
import sys
sys.path.append('../')
from frame.base_handler import BaseHandler


class TFHandler(BaseHandler):
    def __init__(self, conf, data):
        super(TFHandler, self).__init__(conf, data)
        self.factory[self.__class__.__name__] = self
        self.__model = None

    def init(self, params):
        for p in params:
            k, v = p.split(':')
            if k == 'model':
                self.__model = self._data[v]

    def run(self, local_feat, target):
        score = self.__model.query(local_feat, target)
        self._result = {}
        for i in range(len(target)):
            self._result[target[i]] = score[i].tolist()
        return True
