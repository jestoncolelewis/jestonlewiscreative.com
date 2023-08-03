#!/usr/bin/env python3
import os

import aws_cdk as cdk

from s_front_end.pipeline_stack import FrontEndPipeline
from s_front_end.s_front_end_stack import SFrontEndStack


app = cdk.App()
SFrontEndStack(app, "JestonLewisCreativeFrontEndStack", env=cdk.Environment(account="706391136734", region="us-east-1"))
# FrontEndPipeline(app, "JestonLewisCreativeFrontEndStack", env=cdk.Environment(account="706391136734", region="us-east-1"))

app.synth()
