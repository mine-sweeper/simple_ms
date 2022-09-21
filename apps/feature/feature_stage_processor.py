import os
import sys
sys.path.append('../')
from frame.base_stage_processor import BaseStageProcessor
from frame.common import utils


BATCH_SIZE = 2
class FeatureStageProcessor(BaseStageProcessor):
    def __init__(self):
        super(FeatureStageProcessor, self).__init__()
        self.__conf = {}

    def set_conf(self, conf):
        self.__conf.update(conf)

    def split(self, context, subcontext):
        input_feat = context.stage['output']
        local_feat = {x: input_feat[x] for x in self.__conf['input']}
        shared_feat = {x: input_feat[x] for x in self.__conf['input']} if self.__conf['is_shared'] else {}
        num_doc = max([len(x) for x in local_feat.values()]) if not self.__conf['is_shared'] else 1
        for i in range(0, num_doc, BATCH_SIZE):
            tmp_context = context.kage_bunshin()
            tmp_context.stage['local_feature'] = {k: local_feat[k][i:i+BATCH_SIZE] for k in local_feat}
            tmp_context.stage['shared_feature'] = shared_feat
            tmp_context.stage['params'] = context.request.params
            handler = context.handler_factory[self.__conf['handler']].kage_bunshin()
            tmp_context.stage['handler'] = handler
            tmp_context.stage['output'] = {}
            subcontext.append(tmp_context)
        return True

    def process(self, subcontext):
        for sc in subcontext:
            handler = sc.stage['handler']
            shared_feat = sc.stage['shared_feature']
            local_feat = sc.stage['local_feature']
            params = sc.stage['params']
            res = handler.run(local_feat, None)
            sc.stage['output'] = handler.get_result()
        return True

    def merge(self, subcontext, context):
        output = context.stage['output']
        for sc in subcontext:
            res = sc.stage['output']
            for key in res:
                if key not in output:
                    output[key] = res[key]
                else:
                    output[key].extend(res[key])
        return True

