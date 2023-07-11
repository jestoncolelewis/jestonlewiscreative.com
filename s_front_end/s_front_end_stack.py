from constructs import Construct
from aws_cdk import (
    Stack
)
from .hosting import Hosting
from .buckets import Buckets

class SFrontEndStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        buckets = Buckets(self, "Buckets")

        hosting = Hosting(self, "Hosting")
