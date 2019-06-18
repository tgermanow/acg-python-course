import boto3
import click

session = boto3.Session(profile_name='python-course')
ec2 = session.resource('ec2')

@click.command() #@ is decorator/wrapper
def list_instances():
    "List all EC2 intances"
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)))

    return

if __name__ == '__main__':
    list_instances()



