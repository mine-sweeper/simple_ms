import os
import sys
sys.path.append('../')
from frame.base_handler import BaseHandler


class QueryFeatHandler(BaseHandler):
    def __init__(self, conf, data):
        super(QueryFeatHandler, self).__init__(conf, data)
        self.factory[self.__class__.__name__] = self

    def run(self, local_feat, target):
        self._result['q_feat0'] = [1.0]
        self._result['q_feat1'] = [2.0]
        return True

