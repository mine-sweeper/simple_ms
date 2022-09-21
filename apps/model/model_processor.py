import os
import sys
sys.path.append('../')
from frame.base_processor import BaseProcessor
from frame.common import utils
if sys.version_info.major == 2:
    from model_stage_processor import ModelStageProcessor
elif sys.version_info.major == 3:
    from .model_stage_processor import ModelStageProcessor


class ModelProcessor(BaseProcessor):
    def __init__(self):
        super(ModelProcessor, self).__init__()

    def process(self, context):
        for stage in model_stage:
            for component in stage:
                stage_processor.split()
                stage_processor.process()
                stage_processor.merge()
        return True

    def process(self, context):
        biz = context.request.params['biz']
        biz_conf = context.conf.biz_conf
        model_stage = biz_conf[biz]['model']['stage']
        stage_processor = ModelStageProcessor()
        for stage in model_stage:
            for component in stage:
                stage_processor.set_conf(component)
                subcontext = []
                stage_processor.split(context, subcontext)
                stage_processor.process(subcontext)
                stage_processor.merge(subcontext, context)
        return True


