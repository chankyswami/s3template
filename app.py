#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from s3template.s3template_stack import S3Template
app = core.App()
#print(type(app.node.try_get_context("Bucket_Versioning")))
props = {
            'bucket_name':app.node.try_get_context("bucket_name"),
            'bucket_versioning':eval(str(app.node.try_get_context("versioning"))),
            's3_tag1' : app.node.try_get_context("tag_owner"),
            's3_tag2' : app.node.try_get_context("tag_project"),
            'account_number' : app.node.try_get_context("account_number")
            
        }
print(props['bucket_name'])
S3Template(app, "S3TemplateStack", props, env={'account': props['account_number'],'region': 'eu-west-1'})
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=core.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=core.Environment(account='123456789012', region='us-east-1'),
    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html

app.synth()