import boto3
from botocore.exceptions import ClientError

def change_status(region, current_status, new_status):
	ec2 = boto3.client('ec2')

	filter = [
		{
			'Name': 'instance-state-name',
			'Values': [
				current_status,
			]
		},
	]

	ec2_instances = ec2.describe_instance_status(Filters=filter, IncludeAllInstances=True)

	for instance in ec2_instances['InstanceStatuses']:
		if region not in instance['AvailabilityZone']:
			continue
		try:
			if new_status == 'running':
				ec2.start_instances(InstanceIds=[instance['InstanceId']])
			elif new_status == 'reboot':
				ec2.reboot_instances(InstanceIds=[instance['InstanceId']])
			elif new_status == 'stopped':
				ec2.stop_instances(InstanceIds=[instance['InstanceId']])
			elif new_status == 'terminated':
				ec2.terminate_instances(InstanceIds=[instance['InstanceId']])
			print(f"Instance {instance['InstanceId']} is {new_status}")
		except ClientError as error:
			print(error)


change_status("us-east-1c", "running", "terminated")