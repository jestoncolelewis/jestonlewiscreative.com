from constructs import Construct
from aws_cdk import (
    Stage
)
from s_front_end.s_front_end_stack import SFrontEndStack

class BackEndPipeline(Stage):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = SFrontEndStack(self, 'WebService')