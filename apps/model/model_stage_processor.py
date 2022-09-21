import os
import sys
sys.path.append('../')
from frame.base_stage_processor import BaseStageProcessor
from frame.common import utils


BATCH_SIZE = 2
class ModelStageProcessor(BaseStageProcessor):
    def __init__(self):
        super(ModelStageProcessor, self).__init__()
        self.__conf = {}

    def set_conf(self, conf):
        self.__conf.update(conf)

    def split(self, context, subcontext):
        input_feat = context.stage['output']
        num_doc = max([len(x) for x in input_feat.values()]) if not self.__conf['is_shared'] else 1
        for i in range(0, num_doc, BATCH_SIZE):
            tmp_context = context.kage_bunshin()
            tmp_feat = {}
            for feat in self.__conf['input']:
                feat_name = feat['name']
                if feat['is_shared']:
                    tmp_feat[feat_name] = input_feat[feat_name]
                else:
                    tmp_feat[feat_name] = input_feat[feat_name][i:i+BATCH_SIZE]
            tmp_context.stage['input'] = tmp_feat
            handler = context.handler_factory[self.__conf['handler']].kage_bunshin()
            tmp_context.stage['handler'] = handler
            tmp_context.stage['output'] = {}
            subcontext.append(tmp_context)
        return True

    def process(self, subcontext):
        for sc in subcontext:
            handler = sc.stage['handler']
            feat = sc.stage['input']
            handler.init(self.__conf['params'])
            res = handler.run(feat, self.__conf['output'])
            sc.stage['output'] = handler.get_result()
        return True

    def merge(self, subcontext, context):
        output = context.stage['output']
        for sc in subcontext:
            res = sc.stage['output']
            for key in res:
                if key not in output or self.__conf['is_shared']:
                    output[key] = res[key]
                else:
                    output[key].extend(res[key])
        return True

