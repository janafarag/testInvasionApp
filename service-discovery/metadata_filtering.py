import json
import boto3
import pprint

client = boto3.client('servicediscovery')

response = client.discover_instances(
    NamespaceName='cloudmap.private.animalinvasion.com',
    ServiceName='invasion-support',
    MaxResults=100, # ability to return more than 8 IP addresses through API
    QueryParameters={
        'support': 'dogs'
    },
    HealthStatus='HEALTHY' # only return healthy instances
)
pprint.pprint(response.get('Instances'))