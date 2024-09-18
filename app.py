#!/usr/bin/env python3
import os

import aws_cdk as cdk

from django_stack.cdk_stack import NababiRestaurantStack


app = cdk.App()
NababiRestaurantStack(app, "NababiKitchenRestaurantStack")

app.synth()
