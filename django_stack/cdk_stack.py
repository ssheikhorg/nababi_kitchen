import os

from aws_cdk import (
    Duration, Stack,
    # aws_lambda as lambda_,
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

        handler = lambda_python.PythonFunction(
            self,
            f"lambda-{name}",
            description=description,
            runtime=lambda_.Runtime.FROM_IMAGE,  # type: ignore
            handler=lambda_.Handler.FROM_IMAGE,  # type: ignore
            function_name=f"{name}-lambda",
            code=lambda_.Code.from_asset_image(
                directory=os.path.join(os.path.dirname(__file__), ".."),
                file="Dockerfile",
                build_args={"--platform": "linux/amd64"},
            ),
            memory_size=512,
            timeout=Duration.seconds(60),
        )

        # Create HTTP API Gateway (v2)
        http_api = apigwv2.HttpApi(
            self,
            "NababiKitchenApi",
            api_name="NababiKitchenApi",
            description="API for Nababi Kitchen Restaurant",
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
