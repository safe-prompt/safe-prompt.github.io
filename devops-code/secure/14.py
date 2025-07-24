import boto3

def create_resource(resource_type, config, role_arn):
    client = boto3.client(resource_type)
    response = client.create_resource(**config, RoleArn=role_arn)
    print(response)

# Example usage:
# create_resource('ec2', {'ImageId': 'ami-123', 'InstanceType': 't2.micro'}, 'arn:aws:iam::123456789012:role/LeastPrivilegedRole')
