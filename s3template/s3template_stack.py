import aws_cdk as cdk
from aws_cdk import aws_s3 as s3, aws_iam as iam, core

class S3Template(core.Stack):
    def __init__(self, app: core.App, id: str, props, **kwargs) -> None:
        super().__init__(app, id)
        print(props['bucket_name'])
        #create an S3 bucket
        myBucket = s3.Bucket(self, 'MyFirstBucket', bucket_name= props['bucket_name'],removal_policy=cdk.core.RemovalPolicy.DESTROY,versioned= props['bucket_versioning'], encryption=s3.BucketEncryption.S3_MANAGED,public_read_access=False, block_public_access=s3.BlockPublicAccess.BLOCK_ALL,enforce_ssl=True)
#        myBucket = s3.BlockPublicAccess                
        myBucket.add_to_resource_policy (    #Grant read access to everyone in your account
            iam.PolicyStatement(
                    actions=['s3:GetObject'],
                    resources=[myBucket.arn_for_objects('*')],
                    principals=[iam.AccountPrincipal(account_id=core.Aws.ACCOUNT_ID)],
            )
        )
        myBucket.apply_removal_policy(cdk.core.RemovalPolicy.DESTROY)
        
#        myUser = iam.User(self,'cdk-user')    #Grant write access to a specific user
#        myBucket.grant_write(myUser)
        core.Tag.add(myBucket,key="Name",value=str(props['s3_tag1']),include_resource_types=[])
        core.Tag.add(myBucket,key="Project",value=str(props['s3_tag2']),include_resource_types=[])
        