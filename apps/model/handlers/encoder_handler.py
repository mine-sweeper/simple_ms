import os
import sys
sys.path.append('../')
from frame.base_handler import BaseHandler


class Encoder(BaseHandler):
    def __init__(self, conf, data):
        super(Encoder, self).__init__(conf, data)
        self.factory[self.__class__.__name__] = self

    def run(self, local_feat, target):
        foo = lambda x, k: x * k
        if 'q_feat0' in local_feat:
            qf0, qf1 = local_feat['q_feat0'], local_feat['q_feat1']
            self._result['q_vec'] = [qf0[0] * 0.5, qf0[0] * 2, qf1[0] * 0.5, qf1[0] * 2]
        else:
            self._result['d_vec'] = []
            for i in range(len(local_feat['d_feat0'])):
                df0, df1 = local_feat['d_feat0'][i], local_feat['d_feat1'][i]
                self._result['d_vec'].append([foo(df0, 0.5), foo(df0, 2), foo(df1, 0.5), foo(df1, 2)])
        return True

