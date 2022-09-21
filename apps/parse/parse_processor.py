import os
import sys
sys.path.append('../')
from frame.base_processor import BaseProcessor


class ParseProcessor(BaseProcessor):
    def __init__(self):
        super(ParseProcessor, self).__init__()

    def process(self, context):
        req = context.request.url
        params = [kv.split('=') for kv in req.split('&') if kv.count('=') == 1]
        context.request.params.update(params)
        feat = {}
        for kv in context.request.params['feat'].split(';'):
            k, v = kv.split(':')
            feat[k] = v.split(',')
        context.stage['output'] = feat
        return True

