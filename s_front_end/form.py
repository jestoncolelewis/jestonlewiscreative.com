from constructs import Construct
from aws_cdk import (
    aws_lambda as lamb,
    aws_apigateway as api
)

class Form(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        form = lamb.Function(
            self, "Form",
            runtime=lamb.Runtime.PYTHON_3_9,
            code=lamb.Code.from_asset("lambda"),
            handler="form_submit.handler"
        )

        # TODO add permissions for lambda to send emails 

        gateway = api.LambdaRestApi(
            self, "LambdaGateway",
            handler=form
        )
        prod = gateway.root.add_resource("prod")
        prod.add_method("GET")
        prod.add_method("POST")
        prod.add_method("HEAD")