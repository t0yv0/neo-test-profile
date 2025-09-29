"""AWS S3 Bucket Infrastructure using Pulumi"""

import pulumi
from pulumi_aws import s3

# Create an S3 bucket with versioning and encryption
bucket = s3.Bucket(
    "app-bucket",
    # Enable versioning for the bucket
    versioning=s3.BucketVersioningArgs(
        enabled=True,
    ),
    # Enable server-side encryption with AWS managed keys
    server_side_encryption_configuration=s3.BucketServerSideEncryptionConfigurationArgs(
        rule=s3.BucketServerSideEncryptionConfigurationRuleArgs(
            apply_server_side_encryption_by_default=s3.BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs(
                sse_algorithm="AES256",
            ),
        ),
    ),
    # Add tags for organization
    tags={
        "Environment": "dev",
        "ManagedBy": "Pulumi",
        "Project": "neo-test-profile",
    },
)

# Block all public access to the bucket for security
bucket_public_access_block = s3.BucketPublicAccessBlock(
    "app-bucket-pab",
    bucket=bucket.id,
    block_public_acls=True,
    block_public_policy=True,
    ignore_public_acls=True,
    restrict_public_buckets=True,
)

# Export the bucket name and ARN
pulumi.export("bucket_name", bucket.id)
pulumi.export("bucket_arn", bucket.arn)
