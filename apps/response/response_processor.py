import os
import sys
sys.path.append('../')
from frame.base_processor import BaseProcessor


class ResponseProcessor(BaseProcessor):
    def __init__(self):
        super(ResponseProcessor, self).__init__()

    def process(self, context):
        biz = context.request.params['biz']
        biz_conf = context.conf.biz_conf
        res_column = biz_conf[biz]['response']['columns']
        response = {'result': {c: context.stage['output'][c] for c in res_column}}
        context.response = response
        return True

