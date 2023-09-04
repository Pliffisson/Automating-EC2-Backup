import boto3
from datetime import datetime

ec2 = boto3.client('ec2')
current_data = datetime.now().strftime("%d-%m-%y")
try:
    response = ec2.create_snapshot(
        VolumeId='vol-0a897a165b385d5ce',
        Description='Web Server',
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': f"My EC2 snapshot {current_data}"
                    }
                ]
            }
        ]
    )
except Exception as e:
    print(f"Error creating snapshot: {str(e)}")