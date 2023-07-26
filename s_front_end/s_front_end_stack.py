from constructs import Construct
from aws_cdk import (
    Stack
)
from .hosting import Hosting
from .form import Form

class SFrontEndStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        hosting = Hosting(self, "Hosting")
        form = Form(self, "Form")