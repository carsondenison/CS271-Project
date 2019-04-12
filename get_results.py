import boto3

keys = open(file='keys.txt',mode='r').read().splitlines()
MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'


mturk = boto3.client('mturk',
   aws_access_key_id = keys[0],
   aws_secret_access_key = keys[1],
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)

# You will need the following library
# to help parse the XML answers supplied from MTurk
# Install it in your local environment with
# pip install xmltodict
import xmltodict

# Use the hit_id previously created
hit_id_file = 'hit_id.txt'
hit_id = open(file=hit_id_file, mode='r').read()

# We are only publishing this task to one Worker
# So we will get back an array with one item if it has been completed

worker_results = mturk.list_assignments_for_hit(HITId=hit_id, AssignmentStatuses=['Submitted'])
print(worker_results)