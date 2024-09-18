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

        handler = lambda_.DockerImageFunction(
            self, f"{name}-lambda",
            description=f"{description} Lambda Function",
            code=lambda_.DockerImageCode.from_image_asset("."),
            architecture=lambda_.Architecture.ARM_64,
            timeout=Duration.seconds(60),
            memory_size=1024,
        )

        # Create HTTP API Gateway (v2)
        http_api=apigwv2.HttpApi(
            self,
            "NababiKitchenApi",
            api_name="NababiKitchenApi",
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
