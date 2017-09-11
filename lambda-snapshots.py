import boto3
def lambda_handler(event, context):

    volumes = {
        "jenkins" : "vol-02085c8c7e3a46b85"
    }
    
    Client = boto3.client('ec2')
    
    for volume in volumes:
        snapshot = Client.create_snapshot(
          Description='volume %s' % volume,
          VolumeId=volumes[volume],
          DryRun=False
        )
    
        if not snapshot:
            return 'Something happened'    

    return True
