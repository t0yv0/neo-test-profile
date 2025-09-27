"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Create an S3 bucket
bucket = s3.Bucket('app-bucket',
    # Add tags for better resource management
    tags={
        'Environment': 'Testing',
        'ManagedBy': 'Pulumi',
        'Project': 'neo-test-profile',
    },
)

# Enable versioning for the bucket using the recommended approach
bucket_versioning = s3.BucketVersioning('app-bucket-versioning',
    bucket=bucket.id,
    versioning_configuration=s3.BucketVersioningVersioningConfigurationArgs(
        status='Enabled',
    ),
)

# Export the name and ARN of the bucket
pulumi.export('bucket_name', bucket.id)
pulumi.export('bucket_arn', bucket.arn)
