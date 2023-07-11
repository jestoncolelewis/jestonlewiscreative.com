#!/usr/bin/env python3
import os

import aws_cdk as cdk

from s_front_end.pipeline_stack import FrontEndPipeline


app = cdk.App()
FrontEndPipeline(app, "JestonLewisCreativeFrontEndStack", env=cdk.Environment(account="706391136734", region="us-west-2"))

app.synth()
