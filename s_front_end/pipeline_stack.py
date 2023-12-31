from constructs import Construct
from aws_cdk import (
    Stack,
    Environment
)
from aws_cdk.pipelines import (
    CodePipeline,
    CodePipelineSource,
    ShellStep
)

from s_front_end.buckets import name
from s_front_end.pipeline_stage import BackEndPipeline

class FrontEndPipeline(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        pipeline = CodePipeline(
            self, 'Pipeline',
            pipeline_name= 'FrontEndPipeline', 
            synth=ShellStep(
            'Synth',
            input=CodePipelineSource.git_hub('jestoncolelewis/{}'.format(name), 'main'),
            commands= [
                'npm install -g aws-cdk',
                'python -m pip install -r requirements.txt',
                'cdk synth'
            ]
            )
        )

        prod = BackEndPipeline(self, "Prod")
        prod_stage = pipeline.add_stage(prod)