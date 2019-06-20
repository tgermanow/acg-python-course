import boto3
import click

session = boto3.Session(profile_name='python-course')
ec2 = session.resource('ec2')

def filter_instances(owner):
    instances = []

    if owner: 
        filters = [{'Name':'tag:Owner', 'Values':[owner]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances= ec2.instances.all()

    return instances
    

@click.group()
def cli():
    """To manage EC2 instances and snapshots"""
    
@cli.group('volumes')
def volumes():
    """Commands for volumes"""

@cli.group('instances')
def instances():
    """Commands for instances"""


@volumes.command("list")
@click.option('--owner', default=None, help="Only volumes for the owner (tag Owner:<name>)")
def list_volumes(owner):
    "List EC2 volumes" 
    
    instances = filter_instances(owner)
    
    for i in instances:
        for v in i.volumes.all():
            print(", ".join((
                v.id, 
                i.id,
                v.state,
                str(v.size) + "GiB",
                v.encrypted and "Encrypted" or "Not Encrypted"
            )))
            
    return 



@instances.command("list")
@click.option('--owner', default=None, help="Only instances for the owner (tag Owner:<name>)")
def list_instances(owner):
    "List all EC2 intances"
    instances = filter_instances(owner)

    for i in instances:

        # Turning list of tags to dictionary
        tags = {}

        #Option 1: For looping
        # for t in i.tags:
        #    tags[t['Key']] = t['Value']

        # Option 2: dict comprehensions
        # Note the "or []". This is to prevent exception when the there's no tags and None is returned
        tags = { t['Key']: t['Value'] for t in i.tags or []}
        
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)),
            tags.get('Owner', '<no tags defined>')
            )

    return

@instances.command("stop")
@click.option('--owner', default=None, help="Only instances for the Owner")
def stop_instances(owner):
    "Stop EC2 instances"    
    instances = filter_instances(owner)
        
    for i in instances:
        print("Stopping {0}...".format(i.id))
        i.stop()
    
    return
    
    
    
if __name__ == '__main__':
    cli()

