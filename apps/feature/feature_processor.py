import os
import sys
sys.path.append('../')
import sys
from frame.base_processor import BaseProcessor
from frame.common import utils
if sys.version_info.major == 2:
    from feature_stage_processor import FeatureStageProcessor
elif sys.version_info.major == 3:
    from .feature_stage_processor import FeatureStageProcessor


class FeatureProcessor(BaseProcessor):
    def __init__(self):
        super(FeatureProcessor, self).__init__()

    def process(self, context):
        biz = context.request.params['biz']
        biz_conf = context.conf.biz_conf
        feat_stage = biz_conf[biz]['feature']['stage']
        stage_processor = FeatureStageProcessor()
        for stage in feat_stage:
            for component in stage:
                stage_processor.set_conf(component)
                subcontext = []
                stage_processor.split(context, subcontext)
                stage_processor.process(subcontext)
                stage_processor.merge(subcontext, context)
        return True

