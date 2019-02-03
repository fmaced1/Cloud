import boto3
from botocore.exceptions import ClientError
region = 'sa-east-1'

# Enter instances id here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']
instances = ['X-XXXXXXXX',
'X-XXXXXXXX',]

def lambda_handler(event, context):
    for instance in instances:
        ec2 = boto3.client('ec2', region_name=region)
        try:
            ec2.start_instances(InstanceIds=[instance])
            print 'started your instance: ' + str(instance)
        except ClientError as e:
            print 'failed to start EC2 instance in '+str(region)+' region: ' + str(instance)
            print(e)
            pass
