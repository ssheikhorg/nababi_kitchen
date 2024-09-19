import os

from aws_cdk import (
    Duration, Stack,
    aws_lambda as lambda_,
    aws_lambda_python_alpha as lambda_python,
    aws_apigatewayv2 as apigwv2,
    aws_apigatewayv2_integrations as integrations,
    CfnOutput
)
from constructs import Construct


class NababiRestaurantStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        name = "nababi-kitchen-restaurant"
        description = "Nababi Kitchen Restaurant Project"

        lambda_layers = lambda_python.PythonLayerVersion(
            self, f"{name}-layer",
            entry="src/layer", compatible_runtimes=[lambda_.Runtime.PYTHON_3_12],
            layer_version_name=f"{name}-layer",
        )
        handler = lambda_python.PythonFunction(
            self, name,
            function_name=name,
            entry="src", index="restaurant/asgi.py",
            handler="handler",
            memory_size=512, timeout=Duration.minutes(1),
            runtime=lambda_.Runtime.PYTHON_3_12,
            layers=[lambda_layers],
        )

        # Create HTTP API Gateway (v2)
        http_api = apigwv2.HttpApi(
            self, f"{name}-api",
            api_name=f"{name}-api",
            description=f"{description} API Gateway",
        )

        # Define Any Routes
        http_api.add_routes(
            path="/{proxy+}",
            methods=[apigwv2.HttpMethod.ANY],
            integration=integrations.HttpLambdaIntegration(
                f"{name}-integration", handler=handler)  # type: ignore
        )

        # Output the API Gateway URL
        CfnOutput(self, f"{construct_id}-URL", value=http_api.api_endpoint)
