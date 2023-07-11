import aws_cdk as core
import aws_cdk.assertions as assertions

from s_front_end.s_front_end_stack import SFrontEndStack

# example tests. To run these tests, uncomment this file along with the example
# resource in s_front_end/s_front_end_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SFrontEndStack(app, "s-front-end")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
