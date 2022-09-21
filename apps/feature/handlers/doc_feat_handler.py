import os
import sys
sys.path.append('../')
from frame.base_handler import BaseHandler


class DocFeatHandler(BaseHandler):
    def __init__(self, conf, data):
        super(DocFeatHandler, self).__init__(conf, data)
        self.factory[self.__class__.__name__] = self

    def run(self, local_feat, target):
        f0 = [1.0, 2.0, 3.0, 4.0]
        f1 = [-1.0, -2.0, -3.0, -4.0]
        self._result['d_feat0'] = f0[:2] if 'd1' in local_feat['doc'] else f0[2:]
        self._result['d_feat1'] = f1[:2] if 'd1' in local_feat['doc'] else f1[2:]
        return True

